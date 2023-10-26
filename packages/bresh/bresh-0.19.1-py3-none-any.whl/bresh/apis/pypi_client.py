from __future__ import annotations

import re
from pathlib import Path

import requests
from attrs import define, field
from requests import Session
from typing_extensions import Self

from bresh.config import BreshCfg
from bresh.utils.download_file import upload_with_pb

PACKAGE_PATTERN = re.compile(r"<a.+>(.+?)</a>")


@define
class PypiClient:
    _host: str
    _user: str
    _password: str
    _port: int = 8036
    _show_progress: bool = field(default=True, repr=False)

    @classmethod
    def from_cfg(cls, cfg: BreshCfg | None = None) -> Self:
        if not cfg:
            cfg = BreshCfg.load()
        return cls(cfg.cs.host, cfg.pypi.user.secret, cfg.pypi.password.secret)

    @property
    def url(self) -> str:
        return f"http://{self._host}:{self._port}"

    def get_session(self) -> Session:
        s = requests.Session()
        s.auth = (self._user, self._password)
        return s

    def upload(self, path: Path) -> None:
        with self.get_session() as s, path.open("rb") as f:
            data = {
                ":action": "file_upload",
                "protocol_version": "1",
                "content": (path.name, f, "application/octet-stream"),
            }
            headers = {}
            with upload_with_pb(data, headers, show=self._show_progress) as new_data:
                resp = s.post(self.url, data=new_data, headers=headers)
                resp.raise_for_status()

    def list(self) -> list[str]:
        url = f"{self.url}/packages/"
        with self.get_session() as s:
            resp = s.get(url)
            resp.raise_for_status()
            return PACKAGE_PATTERN.findall(resp.text)

    def delete(self, file_name: str) -> None:
        with self.get_session() as s:
            data = {
                ":action": "remove_pkg",
                "name": _get_package_name(file_name),
                "version": _get_package_version(file_name),
            }
            resp = s.post(self.url, data)
            resp.raise_for_status()


def _get_package_name(file_name: str) -> str:
    # cloudshell-logging-1.1.0.zip, cloudshell_logging-1.2.0.3-py2.py3-none-any.whl
    if file_name.endswith(".whl"):
        name = file_name.split("-", 1)[0]
    elif file_name.endswith(".zip") or file_name.endswith(".tar.gz"):
        name = file_name.rsplit("-", 1)[0]
    else:
        raise ValueError(f"Unknown file type: {file_name}")
    return name


def _get_package_version(file_name: str) -> str:
    # cloudshell-logging-1.1.0.zip, cloudshell_logging-1.2.0.3-py2.py3-none-any.whl
    # cloudshell-cp-vcenter-5.0.4.7.tar.gz
    if file_name.endswith(".whl"):
        version = file_name.split("-", 1)[1].split("-")[0]
    elif file_name.endswith(".zip"):
        version = file_name.rsplit("-", 1)[1].removesuffix(".zip")
    elif file_name.endswith(".tar.gz"):
        version = file_name.rsplit("-", 1)[1].removesuffix(".tar.gz")
    else:
        raise ValueError(f"Unknown file type: {file_name}")
    return version


if __name__ == "__main__":
    client = PypiClient.from_cfg()
    packages = client.list()
    print(packages)
    x = packages[0]
    # client.delete(x)
