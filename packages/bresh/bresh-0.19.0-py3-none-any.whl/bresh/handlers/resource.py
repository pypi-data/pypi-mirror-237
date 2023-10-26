from __future__ import annotations

import logging
from typing import Generator, Any

from cloudshell.api import cloudshell_api as auto_api
from typing_extensions import Self
from cloudshell.api.cloudshell_api import (
    ResourceInfo,
    AttributeNameValue,
    ResourceAttributesUpdateRequest,
    InputNameValue,
)

from attrs import define

from bresh.errors import BreshError
from bresh.handlers.base_resource import BaseResource
from bresh.handlers.sandbox import Sandbox


logger = logging.getLogger(__name__)


@define
class ResourceAlreadyExists(BreshError):
    name: str

    def __str__(self):
        return f"Resource '{self.name}' already exists"


@define
class ResourceNotFound(BreshError):
    name: str

    def __str__(self):
        return f"Resource '{self.name}' not found"


@define
class UnsupportedResourceOs(BreshError):
    name: str
    model: str

    def __str__(self):
        return f"Unsupported OS of the '{self.name}' for the Shell '{self.model}'"


@define
class ResourceNotReserved(BreshError):
    name: str

    def __str__(self):
        return f"Resource '{self.name}' is not reserved"


@define
class CommandNotFound(BreshError):
    resource_name: str
    command_name: str

    def __str__(self):
        return (
            f"Command '{self.command_name}' not found for the resource "
            f"'{self.resource_name}'"
        )


@define
class Command:
    name: str
    description: str
    label: str
    parameters: list[CommandParameter]

    @classmethod
    def from_auto_api(cls, command: auto_api.ResourceCommandInfo) -> Self:
        parameters = [CommandParameter.from_auto_api(p) for p in command.Parameters]
        return cls(
            name=command.Name,
            description=command.Description or "",
            label=command.DisplayName,
            parameters=parameters,
        )


@define
class CommandParameter:
    name: str
    description: str
    default: Any
    mandatory: bool
    allowed_values: list[str] | None = None

    @classmethod
    def from_auto_api(cls, param: auto_api.CommandParameter) -> Self:
        options = param.EnumValues.split(",") if param.EnumValues else None
        return cls(
            name=param.Name,
            description=param.Description or "",
            default=param.DefaultValue,
            mandatory=param.Mandatory,
            allowed_values=options,
        )


@define(kw_only=True)
class Resource(BaseResource):
    model: str
    family: str

    @classmethod
    def all(cls) -> Generator[Self, None, None]:
        logger.debug("Getting all resources")
        resources = cls.cs.auto_api.GetResourceList().Resources
        logger.debug(f"Found {len(resources)} resources")
        logger.debug(f"Resources: {resources}")
        for res in resources:
            yield cls(
                name=res.Name,
                model=res.ResourceModelName,
                family=res.ResourceFamilyName,
                address=res.Address,
            )

    @classmethod
    def get(cls, name: str) -> Self:
        try:
            r_info = cls.cs.auto_api.GetResourceDetails(name)
        except auto_api.CloudShellAPIError as e:
            if str(e.code) == "102":
                raise ResourceNotFound(name)
            raise
        return cls.from_resource_info(r_info)

    @classmethod
    def create(
        cls, model: str, name: str, address: str, attrs: dict[str, str] | None = None
    ) -> Self:
        try:
            r_info = cls.cs.auto_api.CreateResource(
                resourceModel=model, resourceName=name, resourceAddress=address
            )
        except auto_api.CloudShellAPIError as e:
            if e.code != 114:
                raise ResourceAlreadyExists(name)
            self = cls.get(name)
        else:
            self = cls.from_resource_info(r_info)

        if attrs:
            self.set_attributes(attrs)
        return self

    @classmethod
    def from_resource_info(cls, info: ResourceInfo) -> Self:
        return cls(
            name=info.Name,
            model=info.ResourceModelName,
            family=info.ResourceFamilyName,
            address=info.Address,
        )

    @property
    def attributes(self) -> dict[str, str]:
        def decrypt(val: str) -> str:
            return self.cs.auto_api.DecryptPassword(val).Value

        attrs = {
            attr.Name: attr.Value if attr.Type != "Password" else decrypt(attr.Value)
            for attr in self._info.ResourceAttributes
        }
        return attrs

    @property
    def in_active_sandbox(self) -> bool:
        return bool(self.sandbox)

    @property
    def sandbox(self) -> Sandbox | None:
        resources = self.cs.auto_api.GetResourceAvailability([self.name]).Resources
        for resource in resources:
            if resource.Name == self.name:
                break
        else:
            # we should never get here
            raise Exception("Resource not found in the response")

        if not (sandboxes := resource.Reservations):
            sandbox = None
        else:
            assert len(sandboxes) == 1
            sandbox = Sandbox(sandboxes[0].ReservationId)
        return sandbox

    def get_attr_by_short_name(self, name: str) -> str:
        for key, val in self.attributes.items():
            if key.endswith(f".{name}"):
                return val
        raise KeyError(name)

    def iter_child(self) -> Generator[Resource, None, None]:
        for child in self._info.ChildResources:
            yield self.cs.Resource.get(child.Name)

    def set_attributes(self, attrs: dict[str, str]) -> None:
        namespace = f"{self.model}."
        attributes = [
            AttributeNameValue(f"{namespace}{key}", value)
            for key, value in attrs.items()
        ]
        self.cs.auto_api.SetAttributesValues(
            [ResourceAttributesUpdateRequest(self.name, attributes)]
        )

    def autoload(self) -> None:
        logger.info(f"Autoloading resource '{self.name}'")
        try:
            self.cs.auto_api.AutoLoad(self.name)
        except auto_api.CloudShellAPIError as e:
            if str(e.code) == "100" and "unsupported device os" in e.message.lower():
                raise UnsupportedResourceOs(self.name, self.model)
            raise

    def execute(self, command: str, **kwargs) -> str:
        sandbox = self.sandbox
        if not sandbox:
            raise ResourceNotReserved(self.name)

        inputs = [InputNameValue(k, v) for k, v in kwargs.items()]
        output = self.cs.auto_api.ExecuteCommand(
            sandbox.id, self.name, "Resource", command, inputs
        ).Output
        return output

    def get_commands(self) -> list[Command]:
        commands = [
            Command.from_auto_api(c)
            for c in self.cs.auto_api.GetResourceCommands(self.name).Commands
        ]
        return commands

    def get_command(self, command_name: str) -> Command:
        commands = self.get_commands()
        try:
            command = next(c for c in commands if c.name == command_name)
        except StopIteration:
            raise CommandNotFound(self.name, command_name)
        return command

    def delete(self) -> None:
        logger.info(f"Deleting resource '{self.name}'")
        self.cs.auto_api.DeleteResource(self.name)
