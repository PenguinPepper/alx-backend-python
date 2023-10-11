#!/usr/bin/env python3
"""module containing wait_n"""

import asyncio
import importlib
from typing import List


wait = importlib.import_module('3-tasks')


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that calls wait_random n times
    """

    new_list = []
    for i in range(n):
        new_list.append(wait.task_wait_random(max_delay))
        completed, pending = await asyncio.wait(new_list)
    sort = [task.result() for task in completed]
    sorted_list = []
    while sort:
        min_value = min(sort)
        sorted_list.append(min_value)
        sort.remove(min_value)
    return sorted_list
