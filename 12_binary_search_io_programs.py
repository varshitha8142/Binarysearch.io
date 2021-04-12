"""
Given an integer n less than or equal to 10, compute its factorial.

The factorial of a number n is defined as n * (n - 1) * (n - 2) * ... * 1.

Example 1
Input

n = 5
Output

120
Explanation

5 * 4 * 3 * 2 * 1 = 120
"""

# paste your solution
class Solution:
    def solve(self, n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
    
