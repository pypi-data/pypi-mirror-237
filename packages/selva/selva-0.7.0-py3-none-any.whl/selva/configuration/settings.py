import os
from collections import UserDict
from copy import deepcopy
from pathlib import Path
from typing import Any

import strictyaml
from loguru import logger

from selva.configuration.defaults import default_settings
from selva.configuration.environment import parse_settings, replace_variables

__all__ = ("Settings", "SettingsError", "get_settings")

SELVA_SETTINGS_ENV = "SELVA_SETTINGS"
DEFAULT_SELVA_SETTINGS = str(Path("configuration") / "settings.yaml")

SELVA_ENV = "SELVA_ENV"


class Settings(UserDict):
    def __init__(self, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = Settings(value)

        super().__init__(data)

    def __getattr__(self, item: str):
        try:
            return self.data[item]
        except KeyError:
            raise AttributeError(item)


class SettingsError(Exception):
    def __init__(self, path: Path):
        super().__init__(f"cannot load settings from {path}")
        self.path = path


def get_settings_for_env(env: str = None) -> dict[str, Any]:
    settings_file_name = "settings"

    settings_file_path = Path(os.getenv(SELVA_SETTINGS_ENV, DEFAULT_SELVA_SETTINGS))

    if env is not None:
        settings_file_name += f"_{env}"
        settings_file_path = settings_file_path.with_stem(
            f"{settings_file_path.stem}_{env}"
        )

    settings_file_path = settings_file_path.absolute()

    try:
        settings_yaml = replace_variables(
            settings_file_path.read_text("utf-8"),
            os.environ,
        )
        return strictyaml.load(settings_yaml).data
    except FileNotFoundError:
        logger.info("settings file not found: {}", settings_file_path)
        return {}
    except (KeyError, ValueError):
        raise
    except Exception as err:
        raise SettingsError(settings_file_path) from err


def merge_recursive(destination: dict, source: dict):
    for key in source:
        if key in destination and all(
            isinstance(arg[key], dict) for arg in (destination, source)
        ):
            merge_recursive(destination[key], source[key])
        else:
            destination[key] = deepcopy(source[key])


def get_settings() -> Settings:
    # get default settings
    settings = deepcopy(default_settings)

    # merge with main settings file (settings.yaml)
    merge_recursive(settings, get_settings_for_env())

    # merge with environment settings file (settings_$SELVA_ENV.yaml)
    if active_env := os.getenv(SELVA_ENV):
        merge_recursive(settings, get_settings_for_env(active_env))

    # merge with environment variables (SELVA_*)
    from_env_vars = parse_settings(os.environ)
    merge_recursive(settings, from_env_vars)

    return Settings(settings)
