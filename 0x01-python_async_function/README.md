#  0x01. Python - Async 

## 1. Async and Await Syntax
The async and await keywords are used to define and work with asynchronous functions in Python.

- async def is used to declare a function as asynchronous.
- await is used to pause the execution of a coroutine until the result of another coroutine is available.

## 2. How to Execute an Async Program with asyncio
- we generally use asyncio.run()

```python
#!/usr/bin/env python3
"""
....
"""
import asyncio

async def say_hello():
    """
    ....
    """
    print("first")
    await  asyncio.sleep(1)
    print("second")
asyncio.run(say_hello())

```
- async def : used to declare a function as async
- await : pasue the exec of a task until the other task is complete. (or we call it coroutine).


## 3. How to Run Concurrent Coroutines
```python

async def task1():
    await asyncio.sleep(1)
    print("Task 1 complete")
async def task2():
    await asyncio.sleep(2)
    print("Task 2 complete")

async def main():
    """
    Run both task concurrent
    """
    await asyncio.gather(task1() ,task2())
asyncio.run(main())
```
- both task1 and task 2 will run concurrently with task1 finish first becasue it has only 1 sec sleep.

## 4. How to Create asyncio Tasks
- we use asyncio.create_task(). This allows coroutines to run concurrently but continue to work in the background without blocking the program.
```python
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
```
## 5. How to Use the random Module
```python

import random
r_n = random.randint(1, 10)
print(f"Random number: {r_n}")
```
