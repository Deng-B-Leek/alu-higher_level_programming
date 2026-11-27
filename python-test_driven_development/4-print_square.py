#!/usr/bin/python3
"""Module for print_square function.
Prints a square of # characters.
Validates size type and value.
"""


def print_square(size):
    """Print a square with #."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
