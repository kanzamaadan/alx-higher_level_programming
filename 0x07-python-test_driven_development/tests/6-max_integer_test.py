#!/usr/bin/python3
"""Unittests for max_integer([..])."""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegers(unittest.TestCase):
    """Unittests for max_integer([..])."""

    def test_ordered_list(self):
        """test ordered list"""
        ord_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ord_list), 4)

    def test_unordered_list(self):
        """test unordered list"""
        unord_list = [1, 6, 2, 4]
        self.assertEqual(max_integer(unord_list), 6)

    def test_beg_list(self):
        """test at the begining the max list"""
        max_beg = [10, 6, 2, 4]
        self.assertEqual(max_integer(max_beg), 10)

    def test_empty_list(self):
        """test empty list"""
        em_list = []
        self.assertEqual(max_integer(em_list), None)

    def test_one_list(self):
        """test one ele list"""
        one_list = [5]
        self.assertEqual(max_integer(one_list), 5)

    def test_float_list(self):
        """test float list"""
        fl_list = [1.3, 5.2, 13.7, 4.3]
        self.assertEqual(max_integer(fl_list), 13.7)

    def test_fl_int_list(self):
        """test float and ints list"""
        fl_list = [1.3, 5, 13.7, 7]
        self.assertEqual(max_integer(fl_list), 13.7)

    def test_str_list(self):
        """test string"""
        string = "solo"
        self.assertEqual(max_integer(string), 's')

    def test_strs_list(self):
        """test strings list"""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_str(self):
        """test empty str"""
        self.assertEqual(max_integer(""), None)
    
if __name__ == '__main__':
    unittest.main()
