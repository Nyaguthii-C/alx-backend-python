#!/usr/bin/env python3
"""Async Comprehensions"""

import asyncio
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[None, None, float]:
    """collect random numbers over async_generator, return random numbers"""
    random_returns = []
    async for i in async_generator():
        random_returns.append(i)
    return random_returns
