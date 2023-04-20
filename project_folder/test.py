import unittest
from fractions import Fraction

from my_sum import sum #imports sum from the other module


class TestSum(unittest.TestCase): # inherits from unittest.TestCase
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data) #call module function and assign to variable
        self.assertEqual(result, 6) # assert the value of result equals 6 using assertEqual()
    
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
