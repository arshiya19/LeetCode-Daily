'''
560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

'''

class Solution(object):
    def subarraySum(self, nums, k):
        hash_map = {0:1} #initilaizing with 0:1 to handle subarrays strating from index 0
        current_sum = 0 
        count = 0

        for num in nums:
            current_sum += num #update the cumulative sum 
            complement = current_sum - k    #check for subarray that sums to k
            #if complement exists in the hash map , add its frequency to the count
            if complement in hash_map:
                count += hash_map[complement]
            
            #update hash map with the current prefix 
            hash_map[current_sum] = hash_map.get(current_sum,0)+1
        
        return count