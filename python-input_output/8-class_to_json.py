#!/usr/bin/python3
"""Returns dict description for JSON serialization."""


def class_to_json(obj):
    """Return dictionary of obj attributes."""
    return obj.__dict__
