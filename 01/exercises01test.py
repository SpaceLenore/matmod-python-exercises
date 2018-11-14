#!/usr/bin/env python3
"""
test exercise 01 functions
"""

import unittest
import exercises01 as matmod

class Testcase(unittest.TestCase):
    """
    Test class using python unittest
    """
    def test_mean(self):
        """ test mean function """
        self.assertEqual(matmod.mean([1, 1, 1, 1, 3, 4, 5]), 2.29)


    def test_variance(self):
        """ test variance function """
        self.assertEqual(matmod.variance([1, 1, 1, 1, 3, 4, 5, 1, 1, 10, 11]), 13.87)

    def test_stddev(self):
        """ test standard deviation """
        self.assertEqual(matmod.stddev([1, 2, -2, 4, -3]), 2.88)

if __name__ == '__main__':
    unittest.main()
