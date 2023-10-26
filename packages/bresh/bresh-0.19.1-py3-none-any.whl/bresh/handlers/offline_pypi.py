from __future__ import annotations

import logging
from pathlib import Path

from alive_progress import alive_it
from attrs import define
from typing_extensions import Self

from bresh.apis.pypi_client import PypiClient
from bresh.config import BreshCfg


logger = logging.getLogger(__name__)


@define
class Pypi:
    _pypi_client: PypiClient

    @classmethod
    def from_cfg(cls, cfg: BreshCfg | None = None) -> Self:
        if cfg is None:
            cfg = BreshCfg.load()
        if not cfg.pypi:
            raise ValueError("No PyPI configuration found")
        client = PypiClient.from_cfg(cfg)
        return cls(client)

    def list(self) -> list[str]:
        return self._pypi_client.list()

    def upload_packages(self, *paths: Path) -> None:
        str_paths = ", ".join(map(str, paths))
        logger.info(f"Uploading {str_paths} to PyPI server {self._pypi_client.url}")
        for path in paths:
            self._pypi_client.upload(path)

    def delete_packages(self, *names: str) -> None:
        logger.info(
            f"Deleting {', '.join(names)} from PyPI server {self._pypi_client.url}"
        )
        bar = alive_it(names)
        for name in bar:
            bar.text(name)
            self._pypi_client.delete(name)

    def clear(self) -> None:
        self.delete_packages(*self.list())
