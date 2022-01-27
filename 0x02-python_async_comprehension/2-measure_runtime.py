#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times
       in parallel using asyncio.gather
       Return : 10 seconds
       """
    start = time.time()
    future_task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*future_task)
    end = time.time()
    total = end - start

    return total
