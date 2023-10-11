#!/usr/bin/env python3
"""
Defines an asynchronous coroutine that takes in an integer argument (max_delay,
with a default value of 10) named wait_random that waits for a random delay
between 0 and max_delay (included and float value) seconds and eventually
returns it.
"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, None] = 10) -> float:
    """waiting for you.."""
    r_delay: float = random.randrange(0, max_delay)
    await asyncio.sleep(r_delay)
    return r_delay


if __name__ == "__main__":
    res = asyncio.run(wait_random(5))
    print(res)
