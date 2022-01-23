#!/usr/bin/env python3
from collections.abc import Callable
import math


def floor(n: float) -> Callable[[math.floor()]]:
    math.floor(n)