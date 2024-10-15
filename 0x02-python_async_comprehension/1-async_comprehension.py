#!/usr/bin/env python3
"""
collecting the random runber from the first task
function
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async generator using building library function"""
    # Async loop over the generated numbers
    return [i async for i in async_generator()]
