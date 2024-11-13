'''
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        current_sum = 0
        minimum_length = float('inf')

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                minimum_length = min(minimum_length, right-left + 1)
                current_sum -= nums[left]
                left += 1
            
        return minimum_length if minimum_length != float('inf') else 0
