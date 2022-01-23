#!/usr/bin/env python3

from collections.abc import Callable

x: Callable[[float, float], float]

def make_multiplier(multiplier: float) -> x:
    return x
