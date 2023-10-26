from __future__ import annotations

import logging
from enum import Enum

logger = logging.getLogger(__name__)


class _NotSet(Enum):
    NOT_SET = "NOT_SET"


NOT_SET = _NotSet.NOT_SET
