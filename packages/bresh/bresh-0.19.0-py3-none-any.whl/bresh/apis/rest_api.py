from __future__ import annotations

import zipfile
from pathlib import Path

import requests
import yaml
from attrs import define, field
from typing_extensions import Self

from bresh.config import BreshCfg
from bresh.utils.download_file import upload_with_pb

API_URL = "http://{host}:9000/API"
LOGIN_URL = f"{API_URL}/Auth/Login"
SHELLS_URL = f"{API_URL}/Shells"


@define
class RestApi:
    _host: str
    _token: str = field(repr=False)
    _show_progress: bool = field(default=True, repr=False)

    @classmethod
    def connect(
        cls, host: str, user: str, password: str, domain: str = "Global"
    ) -> Self:
        url = LOGIN_URL.format(host=host)
        resp = requests.put(
            url, data={"username": user, "password": password, "domain": domain}
        )
        resp.raise_for_status()
        token = resp.text.strip('"')
        return cls(host, token)

    @classmethod
    def from_cfg(cls, cfg: BreshCfg | None = None) -> Self:
        if not cfg:
            cfg = BreshCfg.load()
        return cls.connect(
            cfg.cs.host,
            cfg.cs.user.secret,
            cfg.cs.password.secret,
            cfg.cs.domain,
        )

    @property
    def headers(self) -> dict:
        return {"Authorization": f"Basic {self._token}"}

    def get_shell(self, name: str) -> dict:
        url = SHELLS_URL.format(host=self._host) + f"/{name}"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def add_shell(self, path: Path) -> None:
        url = SHELLS_URL.format(host=self._host)
        headers = self.headers.copy()
        with path.open("rb") as f, upload_with_pb(
            {"files": (path.name, f)}, headers, show=self._show_progress
        ) as new_data:
            resp = requests.post(url, data=new_data, headers=headers)
            resp.raise_for_status()

    def update_shell(self, path: Path, name: str | None = None) -> None:
        name = name or get_shell_name_from_zip(path)
        url = SHELLS_URL.format(host=self._host) + f"/{name}"
        headers = self.headers.copy()
        with path.open("rb") as f, upload_with_pb(
            {"files": (path.name, f)}, headers, show=self._show_progress
        ) as new_data:
            resp = requests.put(url, data=new_data, headers=headers)
            resp.raise_for_status()


def get_shell_name_from_zip(path: Path) -> str:
    with zipfile.ZipFile(path) as zip_file:
        data = yaml.safe_load(zip_file.read("shell-definition.yaml"))

    return data["metadata"]["template_name"]
