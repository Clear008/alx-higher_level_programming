#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for max_integer([..])."""
    def test_n_argum(self):
        """test for no argument"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_ordered_l(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_l(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_identical(self):
        """Test identical value."""
        max_at_beginning = [6, 6, 6, 6]
        self.assertEqual(max_integer(max_at_beginning), 6)

    def test_one_elmnt_list(self):
        """Test a list with one element."""
        one_element = [3]
        self.assertEqual(max_integer(one_element), 3)

    def test_floats(self):
        """Test a list of float numbers."""
        floats = [0.3, -2.6, 5.4, 17.3, 8.9]
        self.assertEqual(max_integer(floats), 17.3)

    def test_float_and_int(self):
        """Test a list of integers and floats."""
        ints_and_floats = [5, 13.93, 11.3, 1]
        self.assertEqual(max_integer(ints_and_floats), 13.93)

    def test_string(self):
        """Test a string."""
        string = "zodiac"
        self.assertEqual(max_integer(string), 'z')


if __name__ == '__main__':
    unittest.main()
