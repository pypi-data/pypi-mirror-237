from __future__ import annotations

import logging
import tempfile
from pathlib import Path
from typing import ClassVar, TYPE_CHECKING, Generator

from attrs import define
from cloudshell.rest.exceptions import ShellNotFound

from bresh.apis.rest_api import get_shell_name_from_zip

if TYPE_CHECKING:
    from bresh.handlers.cs import CloudShell


logger = logging.getLogger(__name__)


@define
class Shell:
    cs: ClassVar[CloudShell]
    id: str
    name: str
    version: str
    is_official: bool

    @classmethod
    def all(cls) -> Generator[Shell, None, None]:
        logger.debug("Getting all shells")
        for shell in cls.cs.portal_api.list_shells():
            logger.debug(f"Found the Shell '{shell['Name']}'")
            yield cls(
                id=shell["Id"],
                name=shell["Name"],
                version=shell["Version"],
                is_official=shell["IsOfficial"],
            )

    @classmethod
    def get(cls, name: str) -> Shell:
        logger.info(f"Getting the Shell '{name}'")
        data = cls.cs.rest_api.get_shell(name)
        return cls(
            id=data["Id"],
            name=data["Name"],
            version=data["Version"],
            is_official=data["IsOfficial"],
        )

    @classmethod
    def upload(cls, path: Path):
        shell_name = get_shell_name_from_zip(path)
        logger.info(f"Installing the Shell {shell_name}")

        try:
            cls.cs.rest_api.update_shell(path, shell_name)
            logger.debug(f"Updated '{shell_name}' Shell")
        except ShellNotFound:
            logger.info(f"The Shell '{shell_name}' is not installed. Installing it")
            cls.cs.rest_api.add_shell(path)
            logger.debug("Installed the Shell '{shell_name}'")

    def download(self, path: Path) -> None:
        logger.info(f"Downloading the Shell '{self.name}'")
        if path.is_dir():
            path = path / f"{self.name}.zip"
        self.cs.portal_api.download_shell(self.id, path)

    def reload(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / f"{self.name}.zip"
            self.download(path)
            self.upload(path)

    def delete(self) -> None:
        logger.info(f"Deleting the Shell '{self.name}'")
        self.cs.rest_api.delete_shell(self.name)
