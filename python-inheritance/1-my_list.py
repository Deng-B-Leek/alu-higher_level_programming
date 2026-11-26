#!/usr/bin/python3
"""MyList class that inherits from list."""


class MyList(list):
    """A list with a print_sorted method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
