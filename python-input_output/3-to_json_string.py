#!/usr/bin/python3
"""Returns JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Return JSON string of my_obj."""
    return json.dumps(my_obj)
