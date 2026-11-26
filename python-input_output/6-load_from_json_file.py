#!/usr/bin/python3
"""Creates object from a JSON file."""
import json


def load_from_json_file(filename):
    """Load Python object from JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
