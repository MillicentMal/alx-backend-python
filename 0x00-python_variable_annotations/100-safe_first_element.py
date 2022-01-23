#!/usr/bin/env python3
"""
correct duck-typed annotations
    """
from types import NoneType
from typing import Any, Iterable, Union


def safe_first_element(lst: Iterable[Any]) -> Union[Any, NoneType]:
    """returns first element of the list Args:lst (Any)
    """
    if lst:
        return lst[0]
    else:
        return None