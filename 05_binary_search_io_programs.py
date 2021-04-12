"""
Given two strings s0 and s1, return whether they are anagrams of each other. Two words are anagrams when you can rearrange one to become the other. For example, "listen" and "silent" are anagrams.

Constraints

n ≤ 100,000 where n is the length of s0
m ≤ 100,000 where m is the length of s1
Example 1
Input

s0 = "listen"
s1 = "silent"
Output

True
"""

# paste your solution
class Solution:
    def solve(self, s0, s1):
        # Write your code here
        n1=len(s0)
        n2=len(s1)
        if n1!= n2 :
            return False
        s0=sorted(s0)
        s1=sorted(s1)
        for i in range(0,n1):
            if(s0[i]!=s1[i]):
                return False
        return True
