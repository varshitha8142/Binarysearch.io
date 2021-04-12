"""
The Fibonacci sequence goes like this: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number can be found by adding up the two numbers before it, and the first two numbers are always 1.

Write a function that takes an integer n and returns the nth Fibonacci number in the sequence.

Note: n will be less than or equal to 30.

Example 1
Input

n = 1
Output

1
Explanation

This is the base case and the first fibonacci number is defined as 1.
"""

# paste your solution
class Solution:
    def solve(self, n):
        # Write your code here
        a=0
        b=1
        if n==1:
            return b
        else:
            for i in range(2,n+1):
                c=a+b
                a=b
                b=c
            return b
