#!/usr/bin/python3
"""Tests for Rectangle - every checker case."""
import io
import os
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Rectangle tests."""

    def test_1_2(self):
        """Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height), (1, 2))

    def test_1_2_3(self):
        """Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_1_2_3_4(self):
        """Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_str_width(self):
        """Rectangle("1", 2)."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_str_height(self):
        """Rectangle(1, "2")."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_str_x(self):
        """Rectangle(1, 2, "3")."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_str_y(self):
        """Rectangle(1, 2, 3, "4")."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_1_2_3_4_5(self):
        """Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_neg_width(self):
        """Rectangle(-1, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_neg_height(self):
        """Rectangle(1, -2)."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zero_width(self):
        """Rectangle(0, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        """Rectangle(1, 0)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_neg_x(self):
        """Rectangle(1, 2, -3)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_neg_y(self):
        """Rectangle(1, 2, 3, -4)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """area()."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        """__str__() Rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_xy(self):
        """display() without x and y."""
        r = Rectangle(2, 2)
        out = io.StringIO()
        sys.stdout = out
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        """display() without y."""
        r = Rectangle(2, 2, 1)
        out = io.StringIO()
        sys.stdout = out
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), " ##\n ##\n")

    def test_display(self):
        """display()."""
        r = Rectangle(2, 3, 2, 2)
        out = io.StringIO()
        sys.stdout = out
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_to_dictionary(self):
        """to_dictionary() Rectangle."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(),
                         {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_update(self):
        """update() Rectangle."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_89(self):
        """update(89)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        """update(89, 1)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_89_1_2(self):
        """update(89, 1, 2)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_89_1_2_3(self):
        """update(89, 1, 2, 3)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_89_1_2_3_4(self):
        """update(89, 1, 2, 3, 4)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    def test_update_kwargs_id(self):
        """update(**{ 'id': 89 })."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        """update(**{ 'id': 89, 'width': 1 })."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_kwargs_id_width_height(self):
        """update(**{ 'id': 89, 'width': 1, 'height': 2 })."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_kwargs_id_width_height_x(self):
        """update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_kwargs_all(self):
        """update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    def test_create_id(self):
        """Rectangle.create(**{ 'id': 89 })."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Rectangle.create(**{ 'id': 89, 'width': 1 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_create_id_width_height(self):
        """Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_create_id_width_height_x(self):
        """Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_create_all(self):
        """Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual((r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    def test_save_none(self):
        """Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty(self):
        """Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_list(self):
        """Rectangle.save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json") as f:
            self.assertIn('"width": 1', f.read())

    def test_load_no_file(self):
        """Rectangle.load_from_file() no file."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_file(self):
        """Rectangle.load_from_file() file exists."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 1)
        self.assertEqual((out[0].width, out[0].height), (1, 2))

if __name__ == "__main__":
    unittest.main()
