'''

2441. Largest Positive Integer That Exists With Its Negative
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.

'''

# My first approach
class Solution(object):
    def findMaxK(self, nums):

        seen = {}
        for i,num in enumerate(nums):
            seen[i] = num 
            largest = max(seen.values())
            neg = -largest
            if neg in seen.values():
                return largest
        
        return -1

#but this didnt work for all the test cases. so below is the corrected code

class Solution(object):
    def findMaxK(self, nums):

        seen = set(nums)

        max_k = -1

        for num in nums:
            if num >0 and -num in seen:
                max_k = max(max_k, num)
        return max_k
