#!/usr/bin/python3
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO
"""This module contains a test suite"""


class TestRectangle(unittest.TestCase):
    """Class containing test suite"""
    def setUp(self):
        """Redirect stdout"""
        sys.stdout = StringIO()

    def tearDown(self):
        """Cleans stream"""
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """Tests for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test(self):
        """Tests for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_documentation(self):
        """Test to see if documentation is created and correct"""
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertTrue(Rectangle.to_dictionary.__doc__)

    def test_id(self):
        """Tests for id"""
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 11)
        R2 = Rectangle(11, 12, 13)
        R3 = Rectangle(12, 13, 14, 15)
        R6 = Rectangle(13, 14, 15, 16, 5)
        R4 = Rectangle(2, 4, 5, 6, 7)
        self.assertEqual(R1.id, 1)
        self.assertEqual(R2.id, 2)
        self.assertEqual(R3.id, 3)
        self.assertEqual(R6.id, 5)
        self.assertEqual(R4.id, 7)

    def test_args(self):
        """Test for checking numbers of objects"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()

    def test_type_error(self):
        """
        Test for check Type Error
        """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)
            Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")
            Rectangle(True, 2)

    def test_value_error(self):
        """
        Test for checking value error
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)
            Rectangle(1, 0)

    def test_area_method(self):
        """
        This test is for testing the area
        method
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(1, 2)
        R2 = Rectangle(2, 3, 4)
        R3 = Rectangle(3, 4, 5, 6)
        self.assertEqual(R1.area(), 2)
        self.assertEqual(R2.area(), 2 * 3)
        self.assertEqual(R3.area(), 3 * 4)

    def test_display(self):
        """
        Test display method. Redirecting stdout to StringIO instance with
        expected output.
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(2, 4)
        R1O = "##\n" \
              "##\n" \
              "##\n" \
              "##\n"
        R2 = Rectangle(2, 3)
        R2O = "##\n" \
              "##\n" \
              "##\n"
        try:
            R1.display()
            self.assertEqual(sys.stdout.getvalue(), R1O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            R2.display()
            self.assertEqual(sys.stdout.getvalue(), R2O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_str(self):
        """
        Test that __str__ method produces correct output.
        """
        Base._Base__nb_objects = 0
        R0 = Rectangle(3, 2, 3)
        self.assertEqual(R0.__str__(), "[Rectangle] (1) 3/0 - 3/2")
        R1 = Rectangle(4, 5, 6, 7, 8)
        self.assertEqual(R1.__str__(), "[Rectangle] (8) 6/7 - 4/5")

    def test_display_with_xy(self):
        """
        Test display method. Redirecting stdout to StringIO instance with
        expected output.
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(2, 3, 2, 2)
        R1O = "\n" \
              "\n" \
              "  ##\n" \
              "  ##\n" \
              "  ##\n"
        R2 = Rectangle(3, 2, 1, 0)
        R2O = " ###\n" \
              " ###\n"
        try:
            R1.display()
            self.assertEqual(sys.stdout.getvalue(), R1O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            R2.display()
            self.assertEqual(sys.stdout.getvalue(), R2O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
