#!/usr/bin/python3
"""
Using TypeVar
"""

from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar, None] = None) -> Union[TypeVar, TypeVar]:
    """
    Using TypeVar
    """
    if key in dct:
        return dct[key]
    else:
        return default
