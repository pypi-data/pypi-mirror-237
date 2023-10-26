from __future__ import annotations

from pathlib import Path
from typing import Any

import keyring
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

from bresh.utils.config_utils import BaseCfg


class KeyRing(str):
    @property
    def secret(self) -> str:
        val = str(self)
        if self.startswith("<") and self.endswith(">") and ":" in self:
            service, account = self.strip("<>").split(":", 1)
            val = keyring.get_password(service, account)
        return val

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(str))


class CloudShell(BaseModel):
    host: str
    user: KeyRing
    password: KeyRing
    domain: str = "Global"

    class Config:
        validate_assignment = True


class OS(BaseModel):
    user: KeyRing
    password: KeyRing

    class Config:
        validate_assignment = True


class SnmpSimulator(BaseModel):
    host: str
    user: KeyRing
    password: KeyRing

    class Config:
        validate_assignment = True


class PypiServer(BaseModel):
    user: KeyRing
    password: KeyRing

    class Config:
        validate_assignment = True


class BreshCfg(BaseCfg):
    cs: CloudShell
    os: OS | None = None
    snmp_simulator: SnmpSimulator | None = None
    pypi: PypiServer | None = None

    class Config(BaseCfg.Config):
        validate_assignment = True
        env_prefix = "BRESH"
        main_path = Path.home() / ".bresh"
        main_cfg_path = main_path / "bresh.toml"
        cfg_folder = main_path / "configs"
