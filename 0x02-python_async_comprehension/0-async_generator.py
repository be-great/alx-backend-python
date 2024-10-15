#!/usr/bin/env python3
"""
generates 10 random numbers asynchronously
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async generator using building library function"""
    for _ in range(10):
        # async wait 1 sec between async objects
        await asyncio.sleep(1)
        # yield similer to return
        # but used to
        #   1-pasue the function for specific time
        #  2- and return that value
        yield random.uniform(0, 10)
