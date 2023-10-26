from __future__ import annotations

from pathlib import Path

from dynaconf import Dynaconf, loaders
from pydantic import BaseModel
from typing_extensions import Self

from bresh.utils.dict_utils import make_all_keys_lower, make_all_keys_upper, merge_dicts


class BaseCfg(BaseModel):
    class Config:
        dynaconf = None
        env_prefix = ""
        main_cfg_path: Path
        cfg_folder: Path
        cfg_ext = "toml"

    @classmethod
    def get_cfg_name(cls) -> str | None:
        conf = Dynaconf(settings_files=[cls.Config.main_cfg_path])
        try:
            name = conf.config_name
        except AttributeError:
            name = None
        return name

    @classmethod
    def set_cfg_name(cls, val: str) -> None:
        path = str(cls.Config.main_cfg_path)
        loaders.write(path, {"CONFIG_NAME": val}, merge=True)

    @classmethod
    def get_cfg_path(cls) -> Path:
        if cfg_name := cls.get_cfg_name():
            file_path = cls.Config.cfg_folder / f"{cfg_name}.{cls.Config.cfg_ext}"
        else:
            file_path = cls.Config.main_cfg_path
        return file_path

    @classmethod
    def get_cfg_names(cls) -> tuple[str]:
        cfg_folder = cls.Config.cfg_folder
        cfg_ext = cls.Config.cfg_ext
        return tuple(p.stem for p in cfg_folder.glob(f"*.{cfg_ext}"))

    @classmethod
    def new_cfg(cls, name: str, from_: str | None) -> None:
        if not from_:
            from_cfg_path = cls.get_cfg_path()
        else:
            from_cfg_path = cls.Config.cfg_folder / f"{from_}.{cls.Config.cfg_ext}"
        new_cfg_path = cls.Config.cfg_folder / f"{name}.{cls.Config.cfg_ext}"
        new_cfg_path.write_text(from_cfg_path.read_text())

    @classmethod
    def load(cls) -> Self:
        dynaconf = Dynaconf(
            settings_files=[cls.get_cfg_path()],
            envvar_prefix=cls.Config.env_prefix,
        )
        data = dynaconf.to_dict()
        data = make_all_keys_lower(data)
        self = cls.model_validate(data)
        self.Config.dynaconf = dynaconf
        return self

    def reload(self) -> None:
        self.Config.dynaconf.reload()
        data = make_all_keys_lower(self.Config.dynaconf.to_dict())
        new_cfg = self.model_validate(data)
        update_model(self, new_cfg.model_dump(exclude_unset=True))

    def get_full_dict(self) -> dict:
        """Get full config from the file and from the memory."""
        new_data = make_all_keys_upper(self.model_dump(exclude_unset=True))
        old_data = self.Config.dynaconf.to_dict()
        old_data = make_all_keys_upper(old_data)
        return merge_dicts(old_data, new_data)

    def save(self) -> None:
        loaders.write(str(self.get_cfg_path()), self.get_full_dict())


def update_model(model: BaseModel, normalized_data: dict) -> None:
    for k, v in normalized_data.items():
        attr = getattr(model, k)
        if isinstance(v, dict) and isinstance(attr, BaseModel):
            update_model(attr, v)
        else:
            setattr(model, k, v)
