#!/usr/bin/env python3
"""
    Returns:
        function: that takes in multiplier and multiplies it with float
    """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returning callable
    """
    return (lambda x: x * multiplier)
