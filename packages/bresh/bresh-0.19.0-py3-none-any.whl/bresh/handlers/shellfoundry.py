import subprocess
from pathlib import Path
from typing import Self

from attrs import define

from bresh.config import BreshCfg


@define
class Shellfoundry:
    host: str

    def __attrs_post_init__(self):
        self.set_host(self.host)

    @classmethod
    def from_cfg(cls, cfg: BreshCfg | None = None) -> Self:
        if cfg is None:
            # load from the default location
            cfg = BreshCfg.load()
        return cls(cfg.cs.host)

    def install(self, path: Path) -> None:
        self._exec("install", cwd=path)

    def get_host(self) -> str:
        output = self._exec("config")
        host = ""
        for line in map(str.strip, output.splitlines()):
            if line.startswith("host "):
                host = line.split(" ", 1)[1].strip()
                break
        return host

    def set_host(self, host: str) -> None:
        self._exec("config", "host", host)

    def _exec(self, command_name: str, *args, cwd: Path | None = None) -> str:
        process = subprocess.Popen(
            ["shellfoundry", command_name, *args],
            stdout=subprocess.PIPE,
            cwd=cwd,
        )
        output, error = process.communicate()
        return output.decode()
