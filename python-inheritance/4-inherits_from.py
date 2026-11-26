#!/usr/bin/python3
"""Check if object inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class, not exactly it."""
    return isinstance(obj, a_class) and type(obj) is not a_class
