"""Given a string s and an integer n, split up s into n-sized pieces.

For example, given:

s = "abcdefg"
n = 3
Return ["abc", "def", "g"].

If there are extra characters left over, they should be in its own piece.

Example 1
Input

s = "abcdef"
n = 2
Output

["ab", "cd", "ef"]

"""

# paste your solution
class Solution:
    def solve(self, s, n):
        # Write your code here
        t=[s[i:i+n]for i in range(0,len(s),n)]
        return t
