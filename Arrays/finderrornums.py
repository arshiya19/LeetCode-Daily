'''
645. Set Mismatch

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
'''

#MY LOGIC -- BUT THE CODE IS VERY SLOW 

class Solution(object):
    def findErrorNums(self, nums):

        nums.sort()
        res = [] #return number occured twice and the missing number
        twice = None #to track 2 element
        missing = None #to add the missing number

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                twice = nums[i]
            
        for num in range(1,len(nums) + 1):
            if num not in nums:
                missing = num
        
        return [twice,missing]


#SO I HAD TO SWITCH TO THE BELOW APPROACH

class Solution(object):
    def findErrorNums(self, nums):

        n = len(nums)

        expected_sum = n*(n+1) //2 #sum of number from 1 to n
        actual_sum = sum(nums)
        actual_no_of_dups = sum(set(nums))

        twice = actual_sum - actual_no_of_dups

        missing = expected_sum - actual_no_of_dups

        return [twice,missing]