'''

3046. Split the Array

You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:

nums1.length == nums2.length == nums.length / 2.
nums1 should contain distinct elements.
nums2 should also contain distinct elements.
Return true if it is possible to split the array, and false otherwise.

Example 1:

Input: nums = [1,1,2,2,3,4]
Output: true
Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].
'''

class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) 
        m = n // 2

        nums1 = [] 
        nums2 = [] 
        for i in range(n):
            if nums[i] not in nums1 and len(nums1) < m:
                nums1.append(nums[i])
            elif nums[i] not in nums2 and len(nums2) < m:
                nums2.append(nums[i])

        return len(nums1) == m and len(nums2) == m
