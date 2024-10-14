#!/usr/bin/env python3
"""
 1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to
    wait_n except task_wait_random is being called.
    """
    # create the n task
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # wait for the tasks to finish
    delays = [await task for task in asyncio.as_completed(tasks)]
    return sorted(delays)
