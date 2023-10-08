#!/usr/bin/env python3
"""stuff"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """split a string"""
    return [(i, len(i)) for i in lst]
