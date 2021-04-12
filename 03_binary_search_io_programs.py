"""
You are given a list nums of length n + 1 picked from the range 1, 2, ..., n. By the pigeonhole principle, there must be a duplicate. Find and return it. There is guaranteed to be exactly one duplicate.

Bonus: Can you do this in linear time and constant space?

Constraints

n ≤ 100,000
Example 1
Input

nums = [1, 2, 3, 1]
Output

1
"""

# paste your solution
class Solution:
    def solve(self, nums):
        # Write your code here
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return nums[i]
            
