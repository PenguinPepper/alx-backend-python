#!/usr/bin/env python3
"""Module has sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """Takes a list mxd_lst of integers and floats
    and returns their sum as a float
    """
    num = 0
    for i in mxd_list:
        num += i
    return num
