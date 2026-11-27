#!/usr/bin/python3
"""Module for add_integer function.
This module provides a function that adds two integers.
It handles type checking and casting of floats to integers.
It raises TypeError for non-integer or non-float inputs.
"""


def add_integer(a, b=98):
    """Add two integers.
    Returns the sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
