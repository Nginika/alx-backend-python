#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function
task_wait_n. The code is nearly identical to wait_n except
task_wait_random is being called.
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n should return the list of all the delays
    (float values). The list of the delays should be in
    ascending order without using sort() because of
    concurrency."""
    task_wait_random(max_delay)
    sorted_list: List[float] = []
    delay_list: List[float] = []
    for i in range(n):
        delay_list.append(wait_random(max_delay))
    for i in asyncio.as_completed(delay_list):
        sorted_list.append(await i)
    return sorted_list
