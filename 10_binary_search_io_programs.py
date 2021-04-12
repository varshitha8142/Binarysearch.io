"""Write a function that rotates a list of numbers to the left by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by 2 becomes [3, 4, 5, 6, 1, 2]. Numbers should wrap around.

Note: The list is guaranteed to have at least one element, and k is guaranteed to be less than or equal to the length of the list.

Bonus: Do this without creating a copy of the list. How many swap or move operations do you need?

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input

nums = [1, 2, 3, 4, 5, 6]
k = 2
Output

[3, 4, 5, 6, 1, 2]

"""

# paste your solution
class Solution:
    def solve(self, nums, k):
        # Write your code here
        l=nums[k:]+nums[:k]
        return l
