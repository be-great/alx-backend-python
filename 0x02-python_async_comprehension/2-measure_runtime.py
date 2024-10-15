#!/usr/bin/env python3
"""
measure the total runtime
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """async generator using building library function"""
    start_time = time.time()
    # to run 4 task async
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.time() - start_time
    return total_time
