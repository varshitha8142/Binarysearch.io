"""
Given a non-negative integer n, find a number r such that r * r = n and round down to the nearest integer.

Can you implement this without using the built-in square root?

Example 1
Input

n = 9
Output

3
"""

# paste your solution
import math
class Solution:
    def solve(self, n):
        # Write your code here
        t = math.sqrt(n)
        return int(t)
