#!/usr/bim/env python3
"""
write an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay.
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n should return the list of all the delays
    (float values). The list of the delays should be in
    ascending order without using sort() because of
    concurrency."""
    sorted_list: List[float] = []
    delay_list: List[float] = []
    for i in range(n):
        delay_list.append(wait_random(max_delay))
    for i in asyncio.as_completed(delay_list):
        sorted_list.append(await i)
    return sorted_list
