# pylint: disable-all

import unittest
import statistics
import numpy as np
from basic_functions import *

class TestBasicFunctions(unittest.TestCase):
    def test_my_mean(self):
        test1 = [5,7,2,2,7,9,30,20,2,6,44,44,4,4,225]
        self.assertEqual(my_mean(test1), statistics.mean(test1))

    def test_my_standard_deviation(self):
        test1 = [5,7,2,2,7,9,30,20,2,6,44,44,4,4,225]
        self.assertEqual(my_standard_deviation(test1), statistics.stdev(test1))

    def test_my_median(self):
        test1 = [5,7,2,2,7,9,30,20,2,6,44,44,4,4,225]
        self.assertEqual(my_median(test1), statistics.median(test1))
        test2 = [5,3,4,6,0,2,1]
        self.assertEqual(my_median(test2), statistics.median(test2))
        test3 = [5,3,4,6,0,2]
        self.assertEqual(my_median(test3), statistics.median(test3))

    def test_my_mode(self):
        test1 = [5,7,2,2,7,9,30,20,2,6,44,44,4,4,225]
        self.assertEqual(my_mode(test1), statistics.mode(test1))
        test2 = ["a","a","b","c"]
        self.assertEqual(my_mode(test2), statistics.mode(test2))
        test3 = [5,3,4,6,0,2,2]
        self.assertEqual(my_mode(test3), statistics.mode(test3))

    def test_my_quartiles(self):
        test1 = [10,22,37,12, 34]
        self.assertEqual(my_quartiles(test1), [11.0, 22, 35.5])
        test2 = [12, 65, 98, 20, 9]
        self.assertEqual(my_quartiles(test2), [10.5, 20, 81.5])
        self.assertEqual(my_quartiles([2,4,9]), [2,4,9])
        self.assertEqual(my_quartiles([2,9]), [2,5.5,9])
