#!/usr/bin/env python3
"""waiting for youuu ..."""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, delay: int) -> float:
    """measure time taken to run wait_n"""
    past = time.time()
    asyncio.run(wait_n(n, delay))

    return (time.time() - past) / n
