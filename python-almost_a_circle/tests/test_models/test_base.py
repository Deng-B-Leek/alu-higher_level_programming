#!/usr/bin/python3
"""Tests for Base - every checker case."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Base tests."""

    def test_auto_id(self):
        """Base() auto id."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_auto_id_plus_one(self):
        """Base() +1 of previous."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """Base(89)."""
        self.assertEqual(Base(89).id, 89)

    def test_to_json_none(self):
        """Base.to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty(self):
        """Base.to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_dict(self):
        """Base.to_json_string([ { 'id': 12 }])."""
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(result, '[{"id": 12}]')
        self.assertIsInstance(result, str)

    def test_from_json_none(self):
        """Base.from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty_list(self):
        """Base.from_json_string("[]")."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_dict(self):
        """Base.from_json_string('[{ "id": 89 }]') returns list."""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{"id": 89}])
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()
