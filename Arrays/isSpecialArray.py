'''
Leetcode - 3151

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.


Firstly -- Initially, I thought I should return based on the length of the array. For example, if the length of the array is 2, I should return False, and if it's 3, I should return True. I ran the code, but 50% of the test cases failed. Then I revisited and understood the code again. I realized that the adjacent numbers should be paired differently, and if they are not, I should return True.


Secondly 

class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)

        i = 0
        j = i+1

        while j < n:

            if (nums[i] % 2 == 0 and nums[j] % 2 == 1) or (nums[i] % 2 == 1 and nums[j] % 2 == 0):
                return True
            i += 1
            j += 1
                    
                
        return False


The while j < n: loop condition works correctly, but the way i and j are incremented together in each iteration could be simplified. 
The current approach involves incrementing both i and j manually, but since j is always one step ahead of i, you can make the code cleaner by only incrementing i and setting j to i + 1.
'''