#!/usr/bin/env python3
"""module with function named wait_random"""


import asyncio
import random


async def wait_random(max_delay: int=10) -> int:
    """
    function that waits for a random delay between 0 and max_delay
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
