#!/usr/bin/env python3
"""
#import async comprehension
import asyncio
import time
#define couroutine measure_time
start time = time.time()
#await asyncio gather using for i in range (4)
end time = time.time()
return endtime -start time
"""

import asyncio
import importlib
import time

com = importlib.import_module('1-async_comprehension')


async def measure_runtime() -> float:
    """measures runtime of comprehension"""
    start_time = time.time()
    await asyncio.gather(com.async_comprehension(), com.async_comprehension(),
            com.async_comprehension(), com.async_comprehension())
    stop_time = time.time()
    return stop_time - start_time
