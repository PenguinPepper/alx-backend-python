#!/usr/bin/env python3
"""module contains async_comprehension"""

import asyncio
import importlib
from typing import List

generator = importlib.import_module('0-async_generator')

async def async_comprehension() -> List[float]:
    """Function returns a float"""
    rand = [i async for i in generator.async_generator()]
    return rand
