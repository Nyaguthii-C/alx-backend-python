#!/usr/bin/env python3
"""
Type-annotated function which takes a list of integers and floats
and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """add up ints and floats in list to return float"""
    sum_mxd_lst = 0.0

    for i in mxd_lst:
        sum_mxd_lst += i
    return sum_mxd_lst
