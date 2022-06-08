#!/usr/bin/env python3
'''
Returning new version of wait_n
'''
import asyncio
from time import time
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """


    Args:
        n (int): Number of times wait_Random is run
        max_delay (int, optional): Maximum delay. Defaults to 0.

    Returns:
        List[float]: Of delays
    """
    wait_list: List[float] = []
    time_delays: List[float] = []
    for i in range(0, n):
        wait_list.append(task_wait_random(max_delay))

    for wait in asyncio.as_completed(wait_list):
        task = await wait
        time_delays.append(task)

    return time_delays
