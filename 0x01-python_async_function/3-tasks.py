#!/usr/bin/env python3
"""module containing task_wait_random"""

import asyncio
import importlib
from typing import Coroutine


wait = importlib.import_module('0-basic_async_syntax')
Task = asyncio.Task


def task_wait_random(max_delay: int) -> Task:
    """
    Function that measures the total exectuion time for wait_n
    """

    return asyncio.create_task(wait.wait_random(max_delay))
