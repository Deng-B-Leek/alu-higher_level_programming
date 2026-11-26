#!/usr/bin/python3
"""Appends a string to a text file (UTF8)."""

def append_write(filename="", text=""):
    """Append text to file, return number of characters added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
