from __future__ import annotations

from pathlib import Path

from attrs import define
from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.rest.api import PackagingRestApiClient

from bresh.config import BreshCfg
from bresh.apis.cs_portal_api import CsPortalApi
from .blueprint import Blueprint as Blueprint_
from .sandbox import Sandbox as Sandbox_
from .resource import Resource as Resource_
from .deployed_app import DeployedApp as DeployedApp_
from .shell import Shell as Shell_
from .app_template import AppTemplate as AppTemplate_


@define
class CloudShell:
    auto_api: CloudShellAPISession
    portal_api: CsPortalApi
    rest_api: PackagingRestApiClient

    @classmethod
    def connect(
        cls, host: str, username: str, password: str, domain: str = "Global"
    ) -> CloudShell:
        api = CloudShellAPISession(host, username, password, domain)
        portal_api = CsPortalApi(host, username, password)
        rest_api = PackagingRestApiClient.login(
            host, username, password, domain, show_progress=True
        )
        return cls(api, portal_api, rest_api)

    @classmethod
    def from_cfg(cls, cfg: BreshCfg | None = None) -> CloudShell:
        if cfg is None:
            # load from the default location
            cfg = BreshCfg.load()
        return cls.connect(
            cfg.cs.host, cfg.cs.user.secret, cfg.cs.password.secret, cfg.cs.domain
        )

    @property
    def Blueprint(self) -> type[Blueprint_]:
        class Blueprint(Blueprint_):
            cs = self

        return Blueprint

    @property
    def Sandbox(self) -> type[Sandbox_]:
        class Sandbox(Sandbox_):
            cs = self

        return Sandbox

    @property
    def Resource(self) -> type[Resource_]:
        class Resource(Resource_):
            cs = self

        return Resource

    @property
    def DeployedApp(self) -> type[DeployedApp_]:
        class DeployedApp(DeployedApp_):
            cs = self

        return DeployedApp

    @property
    def Shell(self) -> type[Shell_]:
        class Shell(Shell_):
            cs = self

        return Shell

    @property
    def AppTemplate(self) -> type[AppTemplate_]:
        class AppTemplate(AppTemplate_):
            cs = self

        return AppTemplate

    @property
    def host(self) -> str:
        return self.auto_api.host

    @property
    def username(self) -> str:
        return self.auto_api.username

    def upload_package(self, path: str | Path) -> None:
        self.rest_api.import_package(path)
