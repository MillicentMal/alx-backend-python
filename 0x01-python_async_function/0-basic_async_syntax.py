#!/usr/bin/env python3
"""
    await_random function
    """
import  asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """[summary]

    Args:
        max_delay (int, optional): Used to delay. Defaults to 10.

    Returns:
        float: number of seconds taken to delay
    """
    
    wait_value = random.uniform(0, max_delay)
    await asyncio.sleep(wait_value)
    return wait_value


print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
