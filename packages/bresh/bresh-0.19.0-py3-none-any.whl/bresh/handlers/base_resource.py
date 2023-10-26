from __future__ import annotations

import logging

from attrs import define
from cloudshell.api.cloudshell_api import ResourceInfo

from bresh.handlers.base_handler import BaseHandler

logger = logging.getLogger(__name__)


@define(kw_only=True)
class BaseResource(BaseHandler):
    name: str
    address: str

    @property
    def _info(self) -> ResourceInfo:
        return self.cs.auto_api.GetResourceDetails(self.name)
