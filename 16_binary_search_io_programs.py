"""
Given an integer n, return a list of integers from 1 to n as strings except for multiples of 3 use “Fizz” instead of the integer and for the multiples of 5 use “Buzz”. For integers which are multiples of both 3 and 5 use “FizzBuzz”.

Example 1
Input

n = 15
Output

["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

"""

# paste your solution
class Solution:
    def solve(self, n):
        # Write your code here
        li=[]
        for i in range(1,n+1):
            i=str(i)
            li.append(i)
        for j in range(0,len(li)):
            i=int(j)
            j=j+1
            if(j%3==0 and j%15!=0):
                li[j-1]="Fizz"
            elif(j%5==0 and j%15!=0):
                li[j-1]="Buzz"
            elif((j%15==0)):
                li[j-1]="FizzBuzz"
        return li
