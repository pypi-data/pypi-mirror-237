from __future__ import annotations

import logging
import time
from collections.abc import Generator
from typing import ClassVar

import requests
from attrs import define, field
from requests import Session
from typing_extensions import Self

from bresh.config import BreshCfg


logger = logging.getLogger(__name__)


@define
class SnmpSimulatorClient:
    host: str
    _username: str = field(repr=False)
    _password: str = field(repr=False)

    @classmethod
    def from_cfg(cls, cfg: BreshCfg | None = None) -> Self:
        if cfg is None:
            cfg = BreshCfg.load()
        if not cfg.snmp_simulator:
            raise ValueError("Config for SNMP Simulator is not provided")
        return cls(
            host=cfg.snmp_simulator.host,
            username=cfg.snmp_simulator.user.secret,
            password=cfg.snmp_simulator.password.secret,
        )

    @property
    def snmp_device(self) -> type[SnmpDevice]:
        class SnmpDevice_(SnmpDevice):
            _client = self

        return SnmpDevice_

    @property
    def api_url(self) -> str:
        return f"http://{self.host}/simulator/api"

    @property
    def recordings_url(self) -> str:
        return f"{self.api_url}/recordings"

    def get_request_session(self) -> Session:
        session = requests.Session()
        session.auth = (self._username, self._password)
        return session


@define
class SnmpDevice:
    _client: ClassVar[SnmpSimulatorClient]
    id: str
    name: str
    ip: str

    @classmethod
    def all(cls) -> Generator[Self, None, None]:
        logger.debug("Getting all SNMP devices")
        with cls._client.get_request_session() as s:
            resp = s.get(cls._client.recordings_url)
            for recording in resp.json():
                yield cls(
                    id=recording["id"],
                    name=recording["name"],
                    ip=recording["ip_address"],
                )

    @classmethod
    def get(cls, id_: int) -> Self:
        with cls._client.get_request_session() as s:
            resp = s.get(f"{cls._client.recordings_url}/{id_}")
            recording = resp.json()
            return cls(
                id=recording["id"],
                name=recording["name"],
                ip=recording["ip_address"],
            )

    @classmethod
    def get_by_ip(cls, ip: str) -> Self:
        logger.info(f"Getting SNMP device by IP '{ip}'")
        for device in cls.all():
            if device.ip == ip:
                return device
        raise ValueError(f"Device with IP '{ip}' not found")

    @property
    def device_url(self) -> str:
        return f"{self._client.recordings_url}/{self.id}"

    def start(self) -> None:
        logger.info(f"Starting SNMP device '{self.name}'")
        with self._client.get_request_session() as s:
            s.get(f"{self.device_url}/start")

    def stop(self) -> None:
        logger.info(f"Stopping SNMP device '{self.name}'")
        with self._client.get_request_session() as s:
            s.get(f"{self.device_url}/stop")

    def reload(self) -> None:
        self.stop()
        time.sleep(1)
        self.start()
