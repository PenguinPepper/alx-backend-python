#!/usr/bin/env python3
"""module containing measure_time"""

import asyncio
import importlib
import time


wait = importlib.import_module('1-concurrent_coroutines')


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that measures the total exectuion time for wait_n
    """

    start = time.time()
    asyncio.run(wait.wait_n(n, max_delay))
    stop = time.time()
    total = stop - start
    return total / n
