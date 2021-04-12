# pylint: disable=invalid-name
"""
Unique Occurrences
Given a list of integers nums, return true
if the number of occurrences of every value
in the array is unique, otherwise return false.
Note: Numbers can be negative.
Example 1
Input
nums = [5, 3, 1, 8, 3, 1, 1, 8, 8, 8]
Output
True
Explanation
Yes, there is 1 occurrence of 5, 2 occurrences of 3,
3 occurrences of 1, and 4 occurrences of 8.
All number of occurrences are unique.
Example 2
Input
nums = [-3, -1, -1, -1, -2, -2]
Output
True
Explanation
There's 1 occurrence of -3, 2 occurrences of -2,
and 3 occurrences of -1. All number of occurrences
are unique.
Example 3
Input
nums = [3, 1, 1, 2, 2, 2, 3]
Output
False
Explanation
There are 2 occurrences of 1, and 2 occurrences of 3.
So the number of occurrences here is not unique.
"""

import unittest
from collections import Counter


# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def unique_occurrences(nums):
	nums=sorted(nums)
	counts = dict(Counter(nums))
	a = counts.values()
	return len(a) == len(set(a))
        

class TestUniqueOccurrences(unittest.TestCase):

    def test_01(self):
        self.assertEqual(unique_occurrences(
            [5, 3, 1, 8, 3, 1, 1, 8, 8, 8]), True)

    def test_02(self):
        self.assertEqual(unique_occurrences([-3, -1, -1, -1, -2, -2]), True)

    def test_03(self):
        self.assertEqual(unique_occurrences([3, 1, 1, 2, 2, 2, 3]), False)

    def test_04(self):
        self.assertEqual(unique_occurrences([1, 2]), False)

    def test_05(self):
        self.assertEqual(unique_occurrences([1, 1, 2, 2, 1]), True)

    def test_06(self):
        self.assertEqual(unique_occurrences(
            [1000, 5, 5, 3333, 1000, 1000]), True)

    def test_07(self):
        self.assertEqual(unique_occurrences(
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]), False)

    def test_08(self):
        self.assertEqual(unique_occurrences(
            [-3, 5, 1, -3, 1, 1, 1, -3, 10, 5]), True)

    def test_09(self):
        self.assertEqual(unique_occurrences(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), False)

    def test_10(self):
        self.assertEqual(unique_occurrences(
            [3, 1, 1, 3, 3, 1, 3, 1, 3, 3, 1, 3]), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
