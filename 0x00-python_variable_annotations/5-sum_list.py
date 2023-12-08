#!/usr/bin/env python3
from typing import List
""" a type annotated function that takes list of float"""
"""and return their sums as float"""


def sum_list(input_list: List[float]) -> float:
    list_sum = 0
    for i in input_list:
        list_sum += i
    return list_sum
