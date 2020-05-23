#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_doc(self):
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]), None)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([7, 1, 10, 16, None])

    def test_one(self):
        self.assertEqual(max_integer([99]), 99)

    def test_integers(self):
        self.assertEqual(max_integer([2, 0, 6, 3]), 6)
        self.assertEqual(max_integer([55, 57, 55, 55]), 57)

    def test_neg(self):
        self.assertEqual(max_integer([-84, -45, -33, -1]), -1)
        self.assertEqual(max_integer([1, 3, 74, -2]), 74)

    def test_float(self):
        self.assertEqual(max_integer([2.2, 3.3, 4, 5.5]), 5.5)
        self.assertEqual(max_integer([-44.5, -53.22, -2.224, -3.14]), -2.224)

    def test_string(self):
        self.assertEqual(max_integer("12345323121"), "5")
        self.assertEqual(max_integer("1, 2, 3"), "3")

    def test_alpha(self):
        self.assertEqual(max_integer(["xyz"]), "xyz")
        self.assertEqual(max_integer(["abc", "1", "4", "xyz"]), "xyz")

    def test_other_type(self):
        self.assertEqual(max_integer([[8, 9, 10], [8, 9, 10]]), [8, 9, 10])

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_docstring(self):
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)


if __name__ == "__main__":
    unittest.main()
