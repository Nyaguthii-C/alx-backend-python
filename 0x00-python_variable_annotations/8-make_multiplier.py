#!/usr/bin/env python3
"""
a type-annotated function that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function to multiply multiplier with a float"""
    def fn_to_multiply(x: float) -> float:
        """takes in a float and multiplies with multiplier"""
        return x * multiplier
    return fn_to_multiply
