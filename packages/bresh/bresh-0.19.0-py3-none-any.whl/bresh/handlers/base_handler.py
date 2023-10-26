from __future__ import annotations

import logging
from typing import TYPE_CHECKING, ClassVar

from attrs import define


if TYPE_CHECKING:
    from bresh import CloudShell


logger = logging.getLogger(__name__)


@define
class BaseHandler:
    cs: ClassVar[CloudShell]
