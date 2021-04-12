"""
Given a positive integer num, return the sum of its digits.

Bonus: Can you do it without using strings?

Example 1
Input

num = 123
Output

6
Explanation

Since 6 = 1 + 2 + 3
"""

# paste your solution
class Solution:
    def solve(self, num):
        # Write your code her
        sum=0
        while(num>0):
            sum+=num%10
            num=num//10
        return sum
