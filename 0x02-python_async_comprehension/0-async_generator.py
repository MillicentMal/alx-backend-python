#!/usr/bin/env python3
"""
        returns an iterator
    """

import asyncio
from random import random

async def async_generator():
    """Async generator 

    Yields:
        list: of random numbers
    """
    for i in range(10):
        asyncio.sleep(1)
        yield random.uniform(0, 10)