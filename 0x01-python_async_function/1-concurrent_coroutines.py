#!/usr/bin/env python3
"""
 1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n should return the list of
    all the delays (float values) sorted by sort()
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
