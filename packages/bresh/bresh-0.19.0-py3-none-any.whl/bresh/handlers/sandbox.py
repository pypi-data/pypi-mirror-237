from __future__ import annotations

import logging
import time
from datetime import datetime, timedelta
from enum import Enum
from typing import ClassVar, TYPE_CHECKING, Generator

from attrs import define
from cached_property import cached_property_ttl
from cloudshell.api.common_cloudshell_api import CloudShellAPIError
from typing_extensions import Self

from bresh.errors import BreshError

if TYPE_CHECKING:
    from cloudshell.api.cloudshell_api import ReservationDescriptionInfo
    from .deployed_app import DeployedApp
    from .cs import CloudShell
    from .resource import Resource


logger = logging.getLogger(__name__)

DATE_TIME_FORMAT = "%m/%d/%Y %H:%M"


@define
class SandboxNotFound(BreshError):
    id: str

    def __str__(self):
        return f"Sandbox {self.id} not found"


@define
class SandboxActiveWithErrors(BreshError):
    id: str

    def __str__(self):
        return f"Sandbox {self.id} is active with errors"


@define
class SandboxCompletedWithErrors(BreshError):
    id: str

    def __str__(self):
        return f"Sandbox {self.id} is completed with errors"


@define
class SandboxCreationTimeout(BreshError):
    id: str

    def __str__(self):
        return f"Sandbox {self.id} creation timeout"


@define
class SandboxFinishingTimeout(BreshError):
    id: str

    def __str__(self):
        return f"Sandbox {self.id} finishing timeout"


class ProvisioningStatus(Enum):
    SETUP = "Setup"
    READY = "Ready"
    TEARDOWN = "Teardown"
    ERROR = "Error"
    NOT_RUN = "Not Run"
    BEFORE_SETUP = "BeforeSetup"


class Status(Enum):
    STARTED = "Started"
    COMPLETED = "Completed"


@define(slots=False)
class Sandbox:
    cs: ClassVar[CloudShell]
    id: str

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()

    @classmethod
    def get(cls, id_: str) -> Self:
        try:
            cls.cs.auto_api.GetReservationDetails(id_)
        except CloudShellAPIError as e:
            if "not exists." in e.message:
                raise SandboxNotFound(id_)
            raise
        return cls(id_)

    @classmethod
    def get_last(cls) -> Self:
        resp = cls.cs.auto_api.GetCurrentReservations(cls.cs.username)
        id_ = resp.Reservations[0].Id
        return cls(id_)

    @classmethod
    def get_alive(cls) -> list[Self]:
        resp = cls.cs.auto_api.GetCurrentReservations(cls.cs.username)
        return [cls(r.Id) for r in resp.Reservations]

    @classmethod
    def create(
        cls,
        name: str,
        blueprint_name: str | None = None,
        duration: int = 60,
        wait: bool = False,
    ) -> Self:
        if blueprint_name:
            logger.info(f"Creating sandbox {name} from blueprint {blueprint_name}")
            res = cls.cs.auto_api.CreateImmediateTopologyReservation(
                name, cls.cs.username, duration, topologyFullPath=blueprint_name
            )
        else:
            logger.info(f"Creating sandbox {name}")
            res = cls.cs.auto_api.CreateImmediateReservation(
                name, cls.cs.username, duration
            )
        id_ = res.Reservation.Id
        self = cls(id_)

        if wait:
            try:
                self.wait_started()
            except CloudShellAPIError:
                self.end()
                raise

        return self

    @property
    def name(self) -> str:
        return self._info.Name

    @property
    def deployed_apps(self) -> Generator[DeployedApp]:
        for r in self._info.Resources:
            if getattr(r, "VmDetails", None):
                yield self.cs.DeployedApp.from_blueprint_info(r)

    @property
    def status(self) -> Status:
        logger.debug(f"Getting status {self}")
        return Status(self._info.Status)

    @property
    def provisioning_status(self) -> ProvisioningStatus:
        logger.debug(f"Getting provisioning status {self}")
        return ProvisioningStatus(self._info.ProvisioningStatus)

    @property
    def end_time(self) -> datetime:
        """Return UTC time."""
        return datetime.strptime(self._info.EndTime, DATE_TIME_FORMAT)

    @property
    def time_left(self) -> timedelta:
        return self.end_time - datetime.utcnow()

    @cached_property_ttl(ttl=5)
    def _info(self) -> ReservationDescriptionInfo:
        return self.cs.auto_api.GetReservationDetails(self.id).ReservationDescription

    def get_deployed_app(
        self, *, name: str = "", name_in_blueprint: str = ""
    ) -> DeployedApp:
        assert name or name_in_blueprint
        for app in self.deployed_apps:
            if name and app.name == name:
                return app
            elif name_in_blueprint and app.name_in_blueprint == name_in_blueprint:
                return app
        raise ValueError(f"Deployed app {name} not found")

    def add_resource(self, *resources: Resource) -> None:
        names = [r.name for r in resources]
        self.cs.auto_api.AddResourcesToReservation(self.id, names)

    def end(self) -> None:
        if self.provisioning_status is not ProvisioningStatus.TEARDOWN:
            self.cs.auto_api.EndReservation(self.id)

    def wait_started(self, timeout: int = 20 * 60) -> None:
        end_time = time.time() + timeout
        while end_time > time.time():
            match self.provisioning_status, self.status:
                case ProvisioningStatus.ERROR, _:
                    raise SandboxActiveWithErrors(self.id)
                case (
                    ProvisioningStatus.NOT_RUN | ProvisioningStatus.READY,
                    Status.STARTED,
                ):
                    break  # sandbox started
                case _:
                    time.sleep(1)
        else:
            raise SandboxCreationTimeout(self.id)

    def wait_finished(self, timeout: int = 20 * 60) -> None:
        end_time = time.time() + timeout
        while end_time > time.time():
            match self.provisioning_status, self.status:
                case ProvisioningStatus.ERROR, Status.COMPLETED:
                    raise SandboxCompletedWithErrors(self.id)
                case ProvisioningStatus.TEARDOWN, Status.COMPLETED:
                    break  # sandbox finished
                case _:
                    time.sleep(1)
        else:
            raise SandboxFinishingTimeout(self.id)

    def iter_errors(self) -> Generator[tuple[str, str], None, None]:
        yield from self.cs.portal_api.iter_sandbox_errors(self.id)
