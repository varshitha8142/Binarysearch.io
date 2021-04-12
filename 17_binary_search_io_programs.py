"""
Given a lowercase alphabet string s, return a string with all the vowels of s in sorted order followed by all the consonants of s in sorted order.

Note: vowels are ["a", "e", "i", "o", "u"] and consonants are all other characters.

Constraints

Length of s ≤ 50000
Example 1
Input

s = "decalin"
Output

"aeicdln"
Explanation

Vowels are "eai" which when sorted is "aei"
Consonants are "dcln" which when sorted is "cdln"
Their concatenation is "aeicdln"


"""

# paste your solution
class Solution:
    def solve(self, s):
        # Write your code here
        k=[]
        v=[]
        for i in s:
            if(i=='a' or i=='e' or i=='i' or i=='u' or i=='o'):
                h=i
                k.append(h)
            else:
                o=i
                v.append(o)

        k.sort()
        v.sort()        
        str1="".join(k)
        str2="".join(v)
        str3=str1+str2
        return str3
