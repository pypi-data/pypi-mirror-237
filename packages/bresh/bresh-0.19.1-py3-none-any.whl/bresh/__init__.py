from pathlib import Path
from .handlers.cs import CloudShell
from .config import BreshCfg

SRC_DIR = Path(__file__).parent
PACKAGE_DIR = SRC_DIR.parent
VERSION_FILE_PATH = PACKAGE_DIR / "version.txt"

with VERSION_FILE_PATH.open() as f:
    __version__ = f.read().strip()


__all__ = (CloudShell, BreshCfg)
