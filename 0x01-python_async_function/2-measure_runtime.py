#!/usr/bin/env python3
"""waiting for youuu ..."""
import time
import asyncio
# from typing import Any, Callable, Coroutine, List

# wait_n: Callable[[int, int], Coroutine[Any, Any, List[float]]] = __import__(
#     '1-concurrent_coroutines').wait_n

wait_n = __import__(
    '1-concurrent_coroutines').wait_n


def measure_time(n: int, delay: int) -> float:
    """measure time taken to run wait_n"""
    past: float = time.time()
    asyncio.run(wait_n(n, delay))
    duration: float = time.time() - past
    true_duration = duration / float(n)

    return true_duration
