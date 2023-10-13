#!/usr/bin/env python3
"""module contains measure_runtime function"""

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
