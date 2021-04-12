"""
Given a string s, return whether it is a palindrome. A palindrome is when the word is the same forwards and backwards.

For example, "tacocat" is a palindrome.

Example 1
Input

s = "racecar"
Output

True
"""

# paste your solution
class Solution:
    def solve(self, s):
        # Write your code here
        x=s[::-1]
        if(s==x):
            return True
        else:
            return False
