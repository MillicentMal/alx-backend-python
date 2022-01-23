#!/usr/bin/env python3
"""
Ducktyping a function that returns length of each item in a list
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Ducktyping each item
    """
    return [(i, len(i)) for i in lst]
