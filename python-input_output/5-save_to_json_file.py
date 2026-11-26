#!/usr/bin/python3
"""Writes object to file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Save my_obj to filename as JSON."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
