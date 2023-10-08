#!/usr/bin/env python3
"""
Write a type-annotated function `sum_list` which takes a list `input_list`
of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """sum and return all elements of the input_list argument."""
    res: float = 0
    for input in input_list:
        res += input

    return res
