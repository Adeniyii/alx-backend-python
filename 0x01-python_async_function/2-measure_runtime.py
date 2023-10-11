#!/usr/bin/env python3
"""waiting for youuu ..."""
import time
import asyncio
from typing import Any, Callable, Coroutine, List
wait_n: Callable[[int, int], Coroutine[Any, Any, List[float]]] = __import__(
    '1-concurrent_coroutines').wait_n


def measure_time(n: int, delay: int) -> float:
    """measure time taken to run wait_n"""
    past: float = time.time()
    asyncio.run(wait_n(n, delay))
    duration: float = time.time() - past

    return duration / n


if __name__ == "__main__":
    n: int = 5
    max_delay: int = 9

    print(measure_time(n, max_delay))
