#!/usr/bin/env python3
""" a type annotated function that takes list of float"""
"""and return their sums as float"""


def sum_list(input_list: [float]) -> float:
    sum = 0
    for i in input_list:
        sum += i
    return sum
# print(sum_list([1.0, 2.0, 3.0]))
