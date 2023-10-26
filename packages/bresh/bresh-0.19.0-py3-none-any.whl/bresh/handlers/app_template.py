from __future__ import annotations

import logging
from typing import TYPE_CHECKING, ClassVar

from attrs import define

from bresh.errors import BreshError

if TYPE_CHECKING:
    from bresh import CloudShell
    from typing_extensions import Self


logger = logging.getLogger(__name__)


@define
class AppTemplateNotFound(BreshError):
    id_or_name: str

    def __str__(self):
        return f"App template {self.id_or_name} not found"


@define
class AppTemplate:
    cs: ClassVar[CloudShell]
    id: str
    name: str
    attributes: dict[str, str]
    deployment_path: str
    cp_name: str

    @classmethod
    def get(cls, id_: str) -> Self:
        logger.debug(f"Getting app template {id}")
        info = cls.cs.portal_api.get_app_data(id_)
        # todo on 404 - raise raise AppTemplateNotFound(id)
        deployment = info["appPaths"][0]["deployment"]
        attrs = {a["Name"]: a["Value"] for a in deployment["attributes"]}
        return cls(
            id=id_,
            name=info["name"],
            attributes=attrs,
            deployment_path=deployment["name"],
            cp_name=deployment["cloudProvider"]["name"],
        )

    @classmethod
    def get_by_name(cls, name: str) -> Self:
        logger.debug(f"Getting app template {name}")
        for a in cls.cs.portal_api.list_app_templates():
            if a["Name"] == name:
                break
        else:
            raise AppTemplateNotFound(name)
        return cls.get(a["Id"])
