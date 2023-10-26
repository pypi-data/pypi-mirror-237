from __future__ import annotations

import logging
import sys
import time
from contextlib import contextmanager, nullcontext
from pathlib import Path
from subprocess import Popen, DEVNULL

from bresh.utils.progress_bar import spinner


logger = logging.getLogger(__name__)


def build_package(
    package_path: Path,
    dist_path: Path | None,
    build_num: bool,
    show_progress: bool = True,
    quiet: bool = False,
) -> set[Path]:
    logger.info(f"Building package {package_path.name}")
    start = time.time()
    python = sys.executable
    if not dist_path:
        dist_path = package_path / "dist"

    cmd = [python, "-m", "build", str(package_path), "-o", str(dist_path)]
    build_context = _add_build_num(package_path) if build_num else nullcontext()

    with build_context, spinner(show_progress):
        if quiet:
            resp = Popen(cmd, stdout=DEVNULL)
        else:
            resp = Popen(cmd)
        resp.wait()
        if resp.returncode:
            raise Exception(resp.returncode)

    new_files = {p for p in dist_path.iterdir() if p.stat().st_mtime > start}
    return new_files


@contextmanager
def _add_build_num(path: Path):
    build_num = _get_new_build_num(path)
    version_path = path / "version.txt"

    # get current version
    orig_version = version_path.read_text()
    version = orig_version.strip()
    assert version.count(".") in (2, 3)

    if version.count(".") == 3:  # remove build number
        version = version.rsplit(".", 1)[0]

    version += f".{build_num}"
    version_path.write_text(version)
    try:
        yield
    finally:
        version_path.write_text(orig_version)


def _get_new_build_num(path: Path) -> int:
    build_num_path = path / "build_num.txt"

    # get current build number
    if not build_num_path.exists():
        build_num = 0
    else:
        build_num = int(build_num_path.read_text())

    build_num += 1

    # save new build number
    with build_num_path.open("w") as f:
        f.write(str(build_num))

    return build_num
