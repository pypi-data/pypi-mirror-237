from __future__ import annotations

import logging
import time
from collections.abc import Generator
from contextlib import contextmanager, suppress
from typing import ClassVar, Self, TYPE_CHECKING

from attrs import define
from cloudshell.api.common_cloudshell_api import CloudShellAPIError

from bresh.apis import package
from bresh.errors import BreshError

if TYPE_CHECKING:
    from bresh.handlers.cs import CloudShell
    from bresh.handlers.sandbox import Sandbox


logger = logging.getLogger(__name__)


@define
class BlueprintNotFound(BreshError):
    full_name: str

    def __str__(self):
        return f"Blueprint {self.full_name} not found"


@define
class DeletionFailedBlueprintInUse(BreshError):
    full_name: str

    def __str__(self):
        return f"Blueprint {self.full_name} is in use cannot delete"


@define
class Blueprint:
    cs: ClassVar[CloudShell]
    full_name: str

    @classmethod
    def all(cls) -> Generator[Self, None, None]:
        logger.debug("Getting all blueprints")
        return (cls(b) for b in cls.cs.auto_api.GetTopologiesByCategory().Topologies)

    @classmethod
    def get(cls, full_name: str) -> Self:
        logger.debug(f"Getting blueprint {full_name}")
        try:
            cls.cs.auto_api.GetTopologyDetails(full_name)
        except CloudShellAPIError as e:
            if e.code == "102":
                raise BlueprintNotFound(full_name)
            raise
        return cls(full_name)

    @classmethod
    @contextmanager
    def create(
        cls,
        name: str,
        description: str = "",
        override: bool = False,
        force: bool = False,
    ) -> package.Blueprint:
        assert not force or (force and override), "force can be use only with override"
        with package.PackageApi.create_package() as p:
            bp = package.Blueprint(name, description=description)
            yield bp
            p.add_blueprint(bp)

            if override:
                with suppress(BlueprintNotFound):
                    bp = cls.get(name)
                    bp.delete(force=force)
                    bp.wait_deleted()
            cls.cs.upload_package(p.zip_path)

    def start(self, wait: bool = False) -> Sandbox:
        return self.cs.Sandbox.create(self.full_name, self.full_name, wait=wait)

    def rename(self, new_name: str) -> None:
        logger.debug(f"Renaming blueprint {self.full_name} to {new_name}")
        self.cs.auto_api.RenameBlueprint(self.full_name, new_name)
        self.full_name = new_name

    def delete(self, *, force: bool = False) -> None:
        logger.debug(f"Deleting blueprint {self.full_name}")
        try:
            self.cs.auto_api.DeleteTopology(self.full_name)
        except CloudShellAPIError:
            if not force:
                raise DeletionFailedBlueprintInUse(self.full_name)

            # end all sandboxes with this blueprint
            resp = self.cs.auto_api.GetCurrentReservations(self.cs.username)
            sandboxes = [
                self.cs.Sandbox.get(sandbox_info.Id)
                for sandbox_info in resp.Reservations
                if self.full_name in sandbox_info.Topologies
            ]
            for sandbox in sandboxes:
                sandbox.end()
            for sandbox in sandboxes:
                sandbox.wait_finished()

            # delete blueprint
            self.cs.auto_api.DeleteTopology(self.full_name)

    def wait_deleted(self, timeout: int = 60) -> None:
        end_time = time.time() + timeout
        while end_time > time.time():
            try:
                self.get(self.full_name)
            except BlueprintNotFound:
                break
            else:
                time.sleep(1)
        else:
            raise TimeoutError(f"Blueprint {self.full_name} was not deleted")
