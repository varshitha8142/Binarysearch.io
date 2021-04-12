"""
Given a positive integer n, sum all of its digits to get a new number. Repeat this operation until it's less than 10.

Example 1
Input

n = 8835
Output

6
Explanation

8 + 8 + 3 + 5 = 24
2 + 4 = 6
        sum=0


 
Accepted
Test case:
8835
Your result:
6
Expected output:
6


"""

# paste your solution
class Solution:
    def solve(self, n):
        # Write your code here
        sum=0
        c=0
        n=str(n)
        for i in n:
            i=int(i)
            sum=sum+i
            c=sum
        if(c>=10):
            while(sum>=10):
                k=sum
                k=str(k)
                sum=0
                for i in k:
                    i=int(i)
                    sum=sum+i
                i=i+1
            return (sum)
        else:
            return (c)
