#!/usr/bin/env python3
"""
    Returns:
        tuple of string and float
    """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns:
        tuple of string and float
    """
    return k, v**2
