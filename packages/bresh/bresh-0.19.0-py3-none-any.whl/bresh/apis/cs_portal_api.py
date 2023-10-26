from __future__ import annotations

import base64
from collections.abc import Generator
from pathlib import Path
from typing import TypedDict

import requests
from attrs import define, field
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from typing_extensions import Self

from bresh.config import BreshCfg
from bresh.utils.download_file import iter_resp_with_pb


class AppTemplateListInfo(TypedDict):
    Id: str
    Name: str


class AppCloudProviderInfo(TypedDict):
    id: str
    name: str


class AppAttributeInfo(TypedDict):
    Id: str
    Name: str
    DisplayName: str
    Description: str
    Value: str
    IsReadOnly: bool
    PossibleValues: list[str]


class AppDeploymentInfo(TypedDict):
    id: str
    name: str
    attributes: list[AppAttributeInfo]
    cloudProvider: AppCloudProviderInfo


class AppPathInfo(TypedDict):
    id: str
    name: str
    deployment: AppDeploymentInfo


class AppTemplateInfo(TypedDict):
    name: str
    appPaths: list[AppPathInfo]


@define
class CsPortalApi:
    _host: str
    _user: str = field(repr=False)
    _password: str = field(repr=False)
    _show_progress: bool = field(default=True, repr=False)
    # not init
    _enc_user: bytes = field(init=False, default=b"", repr=False)
    _enc_password: bytes = field(init=False, default=b"", repr=False)

    @property
    def url(self):
        class Url:
            BASE = f"http://{self._host}"
            API = f"{BASE}/api"
            LOGIN = f"{BASE}/Account/Login"
            PUBLIC_KEY = f"{BASE}/Account/PublicKey"
            SHELLS = f"{API}/shellEntity"
            LIST_SHELLS = f"{SHELLS}/getShells"
            DOWNLOAD_SHELL = f"{SHELLS}/download"
            APPS_URL = f"{API}/appresources"
            APP_URL = f"{APPS_URL}/pagedata/updateapptemplate/{{id}}"
            WORKSPACE_API = f"{API}/WorkspaceApi"
            SANDBOX_ACTIVITIES = (
                f"{WORKSPACE_API}/GetFilteredActivityFeedInfoList?diagramId={{sid}}"
            )
            GET_ACTIVITY = f"{WORKSPACE_API}/GetActivityFeedInfo?eventId={{id}}"

        return Url

    @classmethod
    def from_cfg(cls, cfg: BreshCfg | None = None) -> Self:
        if not cfg:
            cfg = BreshCfg.load()
        return cls(
            cfg.cs.host,
            cfg.cs.user.secret,
            cfg.cs.password.secret,
        )

    @property
    def enc_user(self) -> bytes:
        if not self._enc_user:
            self._set_credentials()
        return self._enc_user

    @property
    def enc_password(self) -> bytes:
        if not self._enc_password:
            self._set_credentials()
        return self._enc_password

    def get_session(self) -> requests.Session:
        s = requests.Session()
        if not self._user:
            self._set_credentials(s)

        s.post(
            self.url.LOGIN,
            data={"username": self.enc_user, "password": self.enc_password},
        )
        return s

    def list_shells(self) -> list[dict]:
        with self.get_session() as s:
            resp = s.get(self.url.LIST_SHELLS)
            resp.raise_for_status()
            return resp.json()["Data"]

    def download_shell(self, id_: str, path: Path) -> None:
        url = self.url.DOWNLOAD_SHELL
        with self.get_session() as s:
            resp = s.get(url, params={"id": id_}, stream=True)
            resp.raise_for_status()

            with path.open("wb") as f:
                for data in iter_resp_with_pb(resp, show=self._show_progress):
                    f.write(data)

    def list_app_templates(self) -> list[AppTemplateListInfo]:
        with self.get_session() as s:
            resp = s.get(self.url.APPS_URL)
            resp.raise_for_status()
            return resp.json()["Data"]

    def get_app_data(self, id_: str) -> AppTemplateInfo:
        with self.get_session() as s:
            resp = s.get(self.url.APP_URL.format(id=id_))
            resp.raise_for_status()
            return resp.json()["Data"]["App"]

    def iter_sandbox_errors(
        self, sandbox_id: str
    ) -> Generator[tuple[str, str], None, None]:
        data = {
            "FromEventId": 0,
            "IsError": True,
        }

        with self.get_session() as s:
            url = self.url.SANDBOX_ACTIVITIES.format(sid=sandbox_id)
            resp = s.post(url, data=data)
            for id_ in [item["Id"] for item in resp.json()["Data"]["Items"]]:
                url = self.url.GET_ACTIVITY.format(id=id_)
                resp = s.get(url)
                data = resp.json()["Data"]
                text = data["Text"]
                output = data["Output"]
                yield text, output

    def _set_credentials(self, session: requests.Session | None = None) -> None:
        s = session or requests.Session()
        resp = s.get(self.url.PUBLIC_KEY)  # download public key
        public_key = serialization.load_pem_public_key(resp.content, default_backend())

        enc_user = public_key.encrypt(self._user.encode(), padding.PKCS1v15())
        self._enc_user = base64.b64encode(enc_user)
        enc_pass = public_key.encrypt(self._password.encode(), padding.PKCS1v15())
        self._enc_password = base64.b64encode(enc_pass)

        if not session:
            s.close()
