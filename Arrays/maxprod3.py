'''
628. Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6

'''

#My first approach 

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        nums.sort(reverse=True)
        n= len(nums) - 1
        
        first_three = nums[:3]

        for num in first_three:
            product *= num
        
        return product
    

'''

The above approach may not work effectively with negative integers. 
Instead, we can sort the array normally and then calculate the product of the last three elements. 
Additionally, for cases involving negative integers, we can calculate the product of the first two elements (the two smallest, most negative numbers) and the largest element at the end of the sorted array. Finally, we return the maximum of these two options.
'''

class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()

        candidate1 = nums[-1]*nums[-2]*nums[-3]

        candidate2 = nums[-1]*nums[0]*nums[1]

        product = max(candidate1,candidate2)

        return product