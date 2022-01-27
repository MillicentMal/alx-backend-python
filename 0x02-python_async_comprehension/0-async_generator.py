#!/usr/bin/env python3
"""
        returns an iterator
    """

import asyncio
from pickletools import float8
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async generator

    Yields:
        list: of random numbers
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
