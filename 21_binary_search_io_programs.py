"""
Given an integer n (where n ≤ 1000), return the sum of the first n positive odd integers.

Example 1
Input

n = 5
Output

25
Explanation

The first 5 odd integers are [1, 3, 5, 7, 9] and its sum is 25.

"""

# paste your solution
# paste your solution
class Solution:
    def solve(self, n):
        # Write your code here
        sum = 0
        curr = 1
        i = 0
        while i < n: 
            sum = sum + curr 
            curr = curr + 2
            i = i + 1
            return sum
