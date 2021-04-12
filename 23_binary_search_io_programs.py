"""
Given a list of strings words, concatenate the strings in camel case format.

Example 1
Input

words = ["java", "beans"]
Output

"javaBeans"
Example 2
Input

words = ["Go", "nasa"]
Output

"goNasa"
"""

# paste your solution
class Solution:
    def solve(self, words):
        # Write your code here
        s = ''
        l=[]
        for i in range(len(words)):
            if(i>0):
                t = words[i].capitalize()
            else:
                t = words[i].lower()
            l.append(t)
        for p in l:
            s = s+p
        return s
