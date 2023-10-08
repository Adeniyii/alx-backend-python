#!/usr/bin/env python3
"""stuff"""

from typing import List


def element_length(lst: List[str]):
    """split a string"""
    return [(i, len(i)) for i in lst]
