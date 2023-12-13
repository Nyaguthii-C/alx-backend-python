#!/usr/bin/env python3
"""Basics of async"""
# import modules
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random number of sec and return the number of sec waited"""
    i: float = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
