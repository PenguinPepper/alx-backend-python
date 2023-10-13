#!/usr/bin/env python3
"""Module contains function named async_generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float]:
    """Function yeilds a andom number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
