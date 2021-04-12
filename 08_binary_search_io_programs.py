"""
Mischievous Number
Question 294 of 745
Given a list of integers nums, return whether there's an integer whose frequency in the list is same as its value.

Example 1
Input

nums = [7, 9, 3, 3, 3]
Output

True
Explanation

The number 3 appears 3 times.
"""

# paste your solution
from collections import Counter
class Solution:
    def solve(self, nums):
        # Write your code here
        t= False
        c=Counter(nums)
        for k,v in c.items():
            if(k==v):
                t=True
        return t
        
