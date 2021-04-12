"""
Given a positive integer num, return the sum of its digits.

Bonus: Can you do it without using strings?

Example 1
Input

num = 123
"""

# paste your solution
class Solution:
    def solve(self, num):
        sum = 0
        while (num!=0):
            sum = sum+int(num%10)
            num = int(num//10)
        return sum
