from __future__ import annotations

from collections.abc import Generator
from pathlib import PurePath, Path

from attrs import define
from typing_extensions import Self

from bresh.config import BreshCfg
from bresh.handlers.smb_client import Smb


QUALI_DIR = PurePath("Program Files (x86)/QualiSystems")
SERVER_DIR = QUALI_DIR / "CloudShell" / "Server"
PYPI_DIR = SERVER_DIR / "Config" / "Pypi Server Repository"


@define
class PypiSmb:
    _smb: Smb

    @classmethod
    def from_cfg(cls, cfg: BreshCfg | None = None) -> Self:
        if cfg is None:
            cfg = BreshCfg.load()
        smb = Smb.from_cfg(cfg)
        return cls(smb)

    def iter_packages(self) -> Generator[str, None, None]:
        return self._smb.iter_filenames(PYPI_DIR, exclude={"PlaceHolder.txt"})

    def upload_packages(self, *paths: Path) -> None:
        self._smb.put_files(PYPI_DIR, *paths)

    def delete_packages(self, *names: str) -> None:
        path = map(PYPI_DIR.joinpath, names)
        self._smb.delete_file(*path)

    def clear(self) -> None:
        self.delete_packages(*self.iter_packages())
