from __future__ import annotations

import socket
from collections.abc import Generator
from typing import ContextManager, Iterable
from pathlib import PurePath, Path

from attrs import define, field
from smb.SMBConnection import SMBConnection
from typing_extensions import Self

from bresh.config import BreshCfg


@define
class Smb:
    host: str
    username: str
    _password: str
    _share: str = "C$"
    _port: int = 445
    _server_name: str = "USER-PC"
    _client_name: str = field(factory=socket.gethostname, init=False)

    @classmethod
    def from_cfg(cls, cfg: BreshCfg | None = None) -> Self:
        if cfg is None:
            cfg = BreshCfg.load()
        if not cfg.os:
            raise ValueError("Config for OS is not provided")
        return cls(
            host=cfg.cs.host,
            username=cfg.os.user.secret,
            password=cfg.os.password.secret,
        )

    def iter_filenames(
        self,
        r_path: PurePath,
        exclude: Iterable[str] | None = None,
    ) -> Generator[str, None, None]:
        r_path = str(r_path)
        excluded = {".", ".."}.union(exclude or [])
        with self._get_connection() as conn:
            for f in conn.listPath(self._share, r_path):
                if f.filename not in excluded:
                    yield f.filename

    def put_file(self, r_path: PurePath, l_path: Path) -> None:
        with self._get_connection() as conn:
            with l_path.open("rb") as f:
                conn.storeFile(self._share, str(r_path), f)

    def put_files(self, r_dir_path: PurePath, *l_paths: Path) -> None:
        with self._get_connection() as conn:
            for l_path in l_paths:
                with l_path.open("rb") as f:
                    r_path = r_dir_path / l_path.name
                    conn.storeFile(self._share, str(r_path), f)

    def delete_file(self, *r_paths: PurePath) -> None:
        with self._get_connection() as conn:
            for path in map(str, r_paths):
                conn.deleteFiles(self._share, path)

    def _get_connection(self) -> ContextManager[SMBConnection]:
        conn = SMBConnection(
            self.username,
            self._password,
            self._client_name,
            self._server_name,
            is_direct_tcp=True,
            use_ntlm_v2=True,
        )
        conn.connect(self.host, self._port)
        return conn
