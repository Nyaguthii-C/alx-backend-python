#!/usr/bin/env python3
"""
a type annotated function that takes list of float
and return their sums as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum the values in list"""
    list_sum = 0.0
    for i in input_list:
        list_sum += i
    return list_sum
