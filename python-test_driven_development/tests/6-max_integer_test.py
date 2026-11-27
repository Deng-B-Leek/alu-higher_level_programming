#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty(self):
        """Test empty list."""
        self.assertIsNone(max_integer([]))

    def test_one(self):
        """Test one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_ordered(self):
        """Test ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        """Test unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test max at beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negatives(self):
        """Test negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_duplicates(self):
        """Test duplicates."""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_no_arg(self):
        """Test no argument."""
        self.assertIsNone(max_integer())

if __name__ == "__main__":
    unittest.main()
