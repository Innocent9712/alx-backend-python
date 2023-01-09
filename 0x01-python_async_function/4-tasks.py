#!/usr/bin/env python3
"""
4. Tasks"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> float:
    """Return the list of all the delays (float values)"""
    delays = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
