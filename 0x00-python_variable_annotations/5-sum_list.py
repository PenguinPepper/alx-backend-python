#!/usr/bin/env python3
"""Module contains function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Tkes in a list and returns the sum all numbers in list
    """
    num = 0
    for i in input_list:
        num += i
    return num
