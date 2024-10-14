#!/usr/bin/env python3
"""
....
"""
import asyncio

# async def say_hello():
#     """
#     ....
#     """
#     print("first")
#     await  asyncio.sleep(1)
#     print("second")
# asyncio.run(say_hello())
# async def task1():
#     await asyncio.sleep(1)
#     print("Task 1 complete")
# async def task2():
#     await asyncio.sleep(2)
#     print("Task 2 complete")

# async def main():
#     """
#     Run both task concurrent
#     """
#     await asyncio.gather(task1() ,task2())
# asyncio.run(main())
async def my_task(n):
    print(f"task {n} started")
    await asyncio.sleep(2)
    print(f"task {n} finish")
async def main():
    task1 = asyncio.create_task(my_task(1))
    task2 = asyncio.create_task(my_task(2))
    # The tasks are running concurrently
    await task1
    await task2

asyncio.run(main())