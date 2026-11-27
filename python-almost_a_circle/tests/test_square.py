#!/usr/bin/python3
"""Tests for Square - every checker case."""
import os
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Square tests."""

    def test_1(self):
        """Square(1)."""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_1_2(self):
        """Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_1_2_3(self):
        """Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_str_size(self):
        """Square("1")."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_str_x(self):
        """Square(1, "2")."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_str_y(self):
        """Square(1, 2, "3")."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_1_2_3_4(self):
        """Square(1, 2, 3, 4)."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_neg(self):
        """Square(-1)."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_neg_x(self):
        """Square(1, -2)."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_neg_y(self):
        """Square(1, 2, -3)."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_zero(self):
        """Square(0)."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """__str__() Square."""
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    def test_to_dictionary(self):
        """to_dictionary() Square."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_update(self):
        """update() Square."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))

    def test_update_89(self):
        """update(89)."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        """update(89, 1)."""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_89_1_2(self):
        """update(89, 1, 2)."""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_89_1_2_3(self):
        """update(89, 1, 2, 3)."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_update_kwargs_id(self):
        """update(**{ 'id': 89 })."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        """update(**{ 'id': 89, 'size': 1 })."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_id_size_x(self):
        """update(**{ 'id': 89, 'size': 1, 'x': 2 })."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_all(self):
        """update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_create_id(self):
        """Square.create(**{ 'id': 89 })."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Square.create(**{ 'id': 89, 'size': 1 })."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_id_size_x(self):
        """Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_all(self):
        """Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_save_none(self):
        """Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty(self):
        """Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_list(self):
        """Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        with open("Square.json") as f:
            self.assertIn('"size": 1', f.read())

    def test_load_no_file(self):
        """Square.load_from_file() no file."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_file(self):
        """Square.load_from_file() file exists."""
        Square.save_to_file([Square(1)])
        out = Square.load_from_file()
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].size, 1)

if __name__ == "__main__":
    unittest.main()
