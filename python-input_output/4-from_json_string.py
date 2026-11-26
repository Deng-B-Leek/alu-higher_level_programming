#!/usr/bin/python3
"""Returns object from JSON string."""
import json

def from_json_string(my_str):
    """Return Python object from JSON string."""
    return json.loads(my_str)
