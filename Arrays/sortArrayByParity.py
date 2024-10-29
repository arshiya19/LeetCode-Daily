'''
905. Sort Array By Parity
Solved
Easy
Topics
Companies
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

'''

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)

        for i in range(n - 1):
            j = i + 1
            while j < n:   
                if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                    nums[i], nums[j] = nums[j] , nums[i]
                j += 1
        
        return nums
    
    

        even = []
        odd = []
        res = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        
        res = even + odd

        return res

        i = 0
        j = n - 1

        while i < j:
            if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j] , nums[i]
                i += 1
                j -= 1
            
            if nums[i] % 2 == 0:
                i += 1
            
            if nums[j] % 2 == 1:
                j -= 1
        
        return nums