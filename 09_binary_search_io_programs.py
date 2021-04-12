"""
Given a list of positive integers nums, return the number of integers that have odd number of digits.

Example 1
Input

nums = [1, 800, 2, 10, 3]
Output

4
Explanation

[1, 800, 2, 3] have odd number of digits.
"""

# paste your solution
class Solution:
    def solve(self, nums):
        # Write your code here
        s=[]
        c=0
        for i in nums:
            i=str(i)
            u=len(i)
            if(u%2!=0):
                c=c+1
        return c
