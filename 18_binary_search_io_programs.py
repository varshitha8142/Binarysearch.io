"""
Given a string s representing a phrase, return its acronym. Acronyms should be capitalized and should not include the word "and".

Example 1
Input

s = "For your information"
Output

"FYI"
"""

# paste your solution
class Solution:
    def solve(self, s):
        # Write your code here
        str=s.split()
        l=[]
        m=""
        for i in range(0,len(str)):
            h=str[i]
            if(h!="and"):
                b=h[0]
                l.append(b)
                m="".join(l)
        return m.upper()
