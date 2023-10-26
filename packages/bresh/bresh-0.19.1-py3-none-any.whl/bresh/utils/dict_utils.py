from __future__ import annotations

from pathlib import Path


def make_all_keys_lower(values: dict) -> dict:
    return change_all_keys(values, str.lower)


def make_all_keys_upper(values: dict) -> dict:
    return change_all_keys(values, str.upper)


def change_all_keys(values: dict, func) -> dict:
    new_values = {}
    for k, v in values.items():
        if isinstance(v, dict):
            v = change_all_keys(v, func)
        new_values[func(k)] = v
    return new_values


def replace_path(values: dict) -> dict:
    new_values = {}
    for k, v in values.items():
        if isinstance(v, dict):
            v = replace_path(v)
        if isinstance(v, Path):
            v = str(v)
        new_values[k] = v
    return new_values


def merge_dicts(*dicts: dict) -> dict:
    """Merge multiple dicts into a new one.

    If there are duplicate keys, the last one wins.
    """
    new_dict = {}
    for d in dicts:
        for k, v in d.items():
            if isinstance(v, dict):
                v = merge_dicts(new_dict.get(k, {}), v)
            new_dict[k] = v
    return new_dict
