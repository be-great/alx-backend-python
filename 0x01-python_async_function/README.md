#  0x01. Python - Async 

## Explaining

Cocurrent code

asyncio is a library to write concurrent code using the async/await syntax.

    run Python coroutines concurrently and have full control over their execution;
    perform network IO and IPC;
    control subprocesses;
    distribute tasks via queues;
    synchronize concurrent code;

Here’s the purpose of each task and why it is useful:

### Task 0: The Basics of Async

    - Point: Introduces how to define and use asynchronous functions in Python.
    - Purpose: It demonstrates the use of async and await to create a coroutine that waits for a random amount of time. This helps you understand how Python’s asyncio module manages tasks that do not block the execution of the program.

### Task 1: Execute Multiple Coroutines Concurrently

    - Point: Demonstrates running multiple coroutines concurrently and managing their results.
    - Purpose: Instead of waiting for each wait_random coroutine to finish one by one, we run multiple instances in parallel. This task helps you understand how to use concurrency (multiple operations happening at the same time) with async programming, making your program more efficient by utilizing asyncio.gather() or similar techniques.

### Task 2: Measure the Runtime

    - Point: Measures the runtime of asynchronous tasks.
    - Purpose: Helps you calculate how much time your asynchronous function (wait_n) takes to complete. By returning the average time per coroutine, you can evaluate the efficiency of your asynchronous operations. This is important when optimizing performance in real-world applications.

### Task 3: Using asyncio.Task

    - Point: Demonstrates how to create tasks using asyncio.create_task().
    - Purpose: Instead of just calling the coroutine, we wrap it in a task using asyncio.Task. This allows the coroutine to run in the background while the rest of the program continues to execute. You can later await the result or let it finish independently. This is useful for parallelizing operations in a non-blocking way.

### Task 4: Tasks with Concurrent Coroutines

    - Point: Extends Task 1 by using asyncio.create_task() from Task 3 to manage coroutines.
    - Purpose: Combines the ideas of running multiple coroutines concurrently (from Task 1) with creating asyncio.Task (from Task 3). The goal is to deepen understanding of how to manage concurrent tasks by creating tasks that run in parallel. It teaches how to control asynchronous execution without blocking your code.

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
