#!/usr/bin/env python3
"""
test exercise 02 functions
"""

import unittest
import exercises02 as f

class Testcase(unittest.TestCase):
    """
    Test class using python unittest
    """

    def test_factorial1(self):
        """ factorial(0) should return 1"""
        self.assertEqual(f.factorial(0), 1)

    def test_factorial2(self):
        """ factorial(5) should return 120"""
        self.assertEqual(f.factorial(5), 120)

    def test_factorial3(self):
        """ factorial(10) should return 3628800"""
        self.assertEqual(f.factorial(10), 3628800)

    def test_binomial1(self):
        """ bin(40, 100, 0.5) should return 0.010 """
        self.assertEqual(f.bin(40, 100, 0.5), 0.011)

    def test_binomial2(self):
        """ bin(150, 200, 0.75) should return 0.065 """
        self.assertEqual(f.bin(150, 200, 0.75), 0.065)

    def test_cumulative_binomial1(self):
        """ cumulative_bin(40, 100, 0.5) should return 0.028 """
        self.assertEqual(f.cumulative_bin(40, 100, 0.5), 0.028)

    def test_cumulative_binomial2(self):
        """ cumulative_bin(150, 200, 0.75) should return 0.527 """
        self.assertEqual(f.cumulative_bin(150, 200, 0.75), 0.527)

if __name__ == '__main__':
    unittest.main()
