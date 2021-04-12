"""
Reverse Words
Question 180 of 744
Given a string of words delimited by spaces, reverse the order of words. For example, given "hello there my friend", return "friend my there hello".

Example 1
Input

sentence = "hello there my friend"
Output

"friend my there hello"
Companies
Topics

"""

# paste your solution
class Solution:
    def solve(self, sentence):
        # Write your code here
        
        words=sentence.split(" ")
        words=list(reversed(words))
        return  (" ".join(words))
        
