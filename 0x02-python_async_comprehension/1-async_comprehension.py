#!/usr/bin/env python3
"""
    Makes use of the generator in async_generator
    """
import asyncio
from pickletools import float8
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Import async_generator from the previous task
    and then write a coroutine called async_comprehension
    that takes no arguments.
    """
    returns = [yielded async for yielded in async_generator()]
    return returns
