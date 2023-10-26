from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Collection
from datetime import datetime, timedelta
from typing import ClassVar, Literal

import xmltodict
from attrs import define, field

from .helpers import AppPositionOnBlueprint, NameGenerator
from bresh.handlers.app_template import AppTemplate


def _create_attributes(
    attributes: dict[str, str], deployment_path=""
) -> dict[str, list[dict[str, str]]]:
    name_space = f"{deployment_path}." if deployment_path else ""
    return {
        "Attribute": [
            {"@Name": f"{name_space}{key}", "@Value": val}
            for key, val in attributes.items()
        ]
    }


def get_bool(v: bool) -> str:
    return str(v).lower()


class XmlNode(ABC):
    @abstractmethod
    def to_xml_dict(self) -> dict:
        raise NotImplementedError()


class XmlRoot(XmlNode):  # todo rename me
    @abstractmethod
    def get_xml_root_dict(self) -> dict:
        raise NotImplementedError()

    def get_xml(self) -> str:
        return xmltodict.unparse(
            self.get_xml_root_dict(), short_empty_elements=True, pretty=True
        )


class MetaData(XmlRoot):
    DEFAULT_CS_VERSION = "2023.2.0"

    def __init__(self, cs_version: str | None = None, now: datetime | None = None):
        self.cs_version = cs_version or self.DEFAULT_CS_VERSION
        self.now = now

    def to_xml_dict(self) -> dict:
        now = self.now or datetime.now() - timedelta(days=1)
        now_str = now.strftime("%d/%m/%Y %H:%M:%S")
        return {
            "CreationDate": now_str,
            "ServerVersion": self.cs_version,
            "PackageType": "CloudShellPackage",
        }

    def get_xml_root_dict(self) -> dict:
        return {
            "Metadata": {
                "@xmlns:xsd": "http://www.w3.org/2001/XMLSchema",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@xmlns": "http://schemas.qualisystems.com/PackageMetadataSchema.xsd",
                **self.to_xml_dict(),
            }
        }


class DeploymentPath(XmlNode):
    def __init__(
        self,
        cp_name: str,
        deployment_path: str,
        attributes: dict[str, str],
    ):
        self.cp_name = cp_name
        self.deployment_path = deployment_path
        self.attributes = attributes
        self.is_default = True

    def to_xml_dict(self) -> dict:
        dp = self.deployment_path
        return {
            "@Name": f"{self.cp_name} - {dp}",
            "@Default": get_bool(self.is_default),
            "DeploymentService": {
                "@Name": dp,
                "@CloudProvider": self.cp_name,
                "Attributes": _create_attributes(self.attributes, dp),
            },
        }


@define
class Service:
    TYPE = "Service"
    name_in_blueprint: str = ""


@define(kw_only=True)
class BlueprintApp(Service, XmlNode):
    DEFAULT_APP_RESOURCE = {
        "@ModelName": "Generic App Model",
        "@Driver": "",
        "Attributes": _create_attributes({"Password": "", "Public IP": "", "User": ""}),
    }
    app_template_name: str
    deployment_paths: list[DeploymentPath]

    def __attrs_post_init__(self):
        if not self.name_in_blueprint:
            self.name_in_blueprint = self.app_template_name

    def to_xml_dict(self) -> dict:
        deployment_paths = [dp.to_xml_dict() for dp in self.deployment_paths]
        return {
            "AppResourceInfo": {
                "@Name": self.name_in_blueprint,
                "AppResources": {"AppResource": [self.DEFAULT_APP_RESOURCE]},
                "DeploymentPaths": {"DeploymentPath": deployment_paths},
            },
        }


@define
class NetworkService(Service, XmlNode):
    SERVICE_NAME: ClassVar[str] = ""
    attrs: dict[str, str] = field(factory=dict)

    def __attrs_post_init__(self):
        if not self.name_in_blueprint:
            self.name_in_blueprint = self.SERVICE_NAME

    def to_xml_dict(self) -> dict:
        return {
            "Attributes": _create_attributes({**self.attrs}),
        }


@define(kw_only=True)
class VlanManual(NetworkService):
    SERVICE_NAME: ClassVar[str] = "VLAN Manual"
    vlan: str

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.attrs["VLAN ID"] = self.vlan


@define
class Connection(XmlNode):
    source: Service
    target: Service
    source_vnic: str | None = None
    target_vnic: str | None = None

    def to_xml_dict(self) -> dict:
        data = {
            "@Source": self.source.name_in_blueprint,
            "@Target": self.target.name_in_blueprint,
            "@Direction": "Bi",
            "@SourceType": self.source.TYPE,
            "@TargetType": self.target.TYPE,
        }

        attrs = []
        if self.source_vnic:
            attrs.append(
                {
                    "Attribute": {
                        "@Name": "Requested Source vNIC Name",
                        "@Value": self.source_vnic,
                    }
                }
            )
        if self.target_vnic:
            attrs.append(
                {
                    "Attribute": {
                        "@Name": "Requested Target vNIC Name",
                        "@Value": self.target_vnic,
                    }
                }
            )
        if attrs:
            data["Attributes"] = attrs

        return data


@define
class Attribute(XmlNode):
    name: str
    type: Literal["String", "Boolean", "Password"]
    default: str = ""
    read_only: bool = False

    def to_xml_dict(self) -> dict:
        data = {
            "@Name": self.name,
            "@Type": self.type,
            "@DefaultValue": self.default,
            "@IsReadOnly": str(self.read_only).lower(),
            "Rules": {"Rule": [{"@Name": "Configuration"}]},
        }
        return data


@define
class DataModel(XmlRoot):
    attrs: Collection[Attribute]

    def to_xml_dict(self) -> dict:
        return {"Attributes": {"AttributeInfo": [a.to_xml_dict() for a in self.attrs]}}

    def get_xml_root_dict(self) -> dict:
        data = {
            "DataModelInfo": {
                "@xmlns:xsd": "http://www.w3.org/2001/XMLSchema",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "@xmlns": "http://schemas.qualisystems.com/ResourceManagement/DataModelSchema.xsd",
                **self.to_xml_dict(),
            }
        }
        return data


@define
class Blueprint(XmlRoot):
    name: str
    description: str = ""
    _services: list[NetworkService] = field(factory=list)
    _apps: list[BlueprintApp] = field(factory=list)
    _position_gen: AppPositionOnBlueprint = field(
        init=False, factory=AppPositionOnBlueprint
    )
    _name_gen: NameGenerator = field(init=False, factory=NameGenerator)
    _connections: list[Connection] = field(factory=list)

    def add_app(
        self, app: BlueprintApp | AppTemplate, attrs: dict[str, str] | None = None
    ) -> BlueprintApp:
        # from bresh.handlers.app_template import AppTemplate
        if isinstance(app, AppTemplate):
            attrs = {**app.attributes, **(attrs or {})}
            dp = DeploymentPath(app.cp_name, app.deployment_path, attrs)
            app = BlueprintApp(
                app_template_name=app.name,
                deployment_paths=[dp],
            )
        app.name_in_blueprint = self._name_gen(app.name_in_blueprint)
        self._apps.append(app)
        return app

    def add_vlan_manual(
        self, vlan: str | int, alias: str = "", attrs: dict[str, str] | None = None
    ) -> VlanManual:
        attrs = attrs or {}
        vlan_service = VlanManual(vlan=str(vlan), attrs=attrs, name_in_blueprint=alias)
        self.add_network_service(vlan_service)
        return vlan_service

    def connect(
        self,
        source: Service,
        target: Service,
        source_vnic: str | None = None,
        target_vnic: str | None = None,
    ) -> None:
        conn = Connection(source, target, source_vnic, target_vnic)
        self._connections.append(conn)

    def add_network_service(self, service: NetworkService) -> None:
        service.name_in_blueprint = self._name_gen(service.name_in_blueprint)
        self._services.append(service)

    def to_xml_dict(self) -> dict:
        return {
            "Details": {
                "@Name": self.name,
                "@Public": "false",
                "@Driver": "Python Setup & Teardown",
                "@SetupDuration": "10",
                "@TeardownDuration": "10",
                "@EnableSandboxSave": "true",
                "Description": self.description,
                "Scripts": {
                    "Script": [
                        {"@Name": "Default Sandbox Save 4.0"},
                        {"@Name": "Default Sandbox Restore 4.0"},
                        {"@Name": "Default Sandbox Setup 4.0"},
                        {"@Name": "Default Sandbox Teardown 4.0"},
                    ]
                },
            }
        }

    def get_xml_root_dict(self) -> dict:
        data = {
            "TopologyInfo": {
                "@xmlns:xsd": "http://www.w3.org/2001/XMLSchema",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                **self.to_xml_dict(),
            }
        }
        if sd := self._get_services_dict():
            data["TopologyInfo"]["Services"] = {"Service": sd}
        if ad := self._get_apps_dict():
            data["TopologyInfo"]["Apps"] = {"App": ad}
        if cd := [c.to_xml_dict() for c in self._connections]:
            data["TopologyInfo"]["Routes"] = {"Connector": cd}
        return data

    def _get_new_position(self):
        x, y = self._position_gen.get_new_position()
        return {"@PositionX": str(x), "@PositionY": str(y)}

    def _get_apps_dict(self) -> list[dict]:
        for app in self._apps:
            # set first DP to be default
            app.deployment_paths[0].is_default = True

        return [
            {
                **self._get_new_position(),
                "@TemplateName": app.app_template_name,
                **app.to_xml_dict(),
            }
            for app in self._apps
        ]

    def _get_services_dict(self) -> list[dict]:
        return [
            {
                **self._get_new_position(),
                "@Alias": service.name_in_blueprint,
                "@ServiceName": service.SERVICE_NAME,
                **service.to_xml_dict(),
            }
            for service in self._services
        ]
