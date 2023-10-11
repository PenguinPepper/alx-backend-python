#!/usr/bin/env python3
"""module containing wait_n"""

import asyncio
import importlib
from typing import List


wait = importlib.import_module('0-basic_async_syntax')


async def wait_n(n: int, min_delay: int) -> List[float]:
    """
    Function that calls wait_random n times
    """

    new_list = []
    for i in range(n):
        new_list.append(asyncio.create_task(wait.wait_random(min_delay)))
        completed, pending = await asyncio.wait(new_list)
    sort = [task.result() for task in completed]
    sorted_list = []
    while sort:
        min_value = min(sort)
        sorted_list.append(min_value)
        sort.remove(min_value)
    return sorted_list
