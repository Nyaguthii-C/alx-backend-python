#!/usr/bin/env python3
"""A function that takes mixed type input to return a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
     """square the int or float input and return as tuple with string""" 
     return (k, v * v)
