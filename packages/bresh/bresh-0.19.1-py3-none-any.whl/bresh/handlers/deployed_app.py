from typing import Self

from attrs import define
from cloudshell.api.cloudshell_api import ReservedResourceInfo

from bresh.handlers.base_resource import BaseResource


@define
class DeployedApp(BaseResource):
    name_in_blueprint: str
    uuid: str

    @classmethod
    def from_blueprint_info(cls, r_info: ReservedResourceInfo) -> Self:
        return cls(
            name=r_info.Name,
            name_in_blueprint=r_info.AppDetails.AppName,
            uuid=r_info.VmDetails.UID,
            address=r_info.FullAddress,
        )
