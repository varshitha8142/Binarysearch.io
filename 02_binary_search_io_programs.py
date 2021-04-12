"""
Paste the question with examples
Given a list of integers nums, a string op representing either "+", "-", "/", or "*", and an integer val, perform the operation on every number in nums with val and return the result.

Note: "/" is integer division.

Example 1
Input

nums = [3, 1, 6]
op = "+"
val = 4
Output

[7, 5, 10]
Explanation

We add 4 to every number in nums and return it.
"""

# paste your solution
class Solution:
    def solve(self, nums, op, val):
        # Write your code here
        list=[]
        for n in nums:
            if(op=='+'):
               list.append(n+val)
            if(op=='-'):
               list.append(n-val)
            if(op=='/'):
               list.append(n//val)
            if(op=='*'):
               list.append(n*val)
        return list
