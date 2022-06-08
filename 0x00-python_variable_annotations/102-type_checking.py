#!/usr/bin/env python3
"""
Fixing typng using mypy
"""
from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    mypy used to fix typing errors
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
