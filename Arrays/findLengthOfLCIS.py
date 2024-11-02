'''
674. Longest Continuous Increasing Subsequence
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
'''

#Understanding here why i am firstly initilasing maxlength and currentlength to 1

'''

Initial Value of current_length = 1:

We start counting each subsequence from 1 because any single element is itself a "subsequence" of length 1.
This way, if the array only has one element or if all elements are the same, we’ll still count that single element or each subsequence correctly as starting from 1.
Initial Value of max_length = 1:

Similarly, we initialize max_length to 1 because if there’s at least one element in the array, the smallest possible "longest increasing subsequence" is 1 (the element itself).
This ensures that we have a valid starting value for max_length even before we process the list.
Why Not Start From 0?
Starting from 0 would mean we’re assuming no valid subsequence exists initially, which could complicate our logic, especially for cases like single-element arrays. Setting both current_length and max_length to 1 makes it simpler and more intuitive to handle cases where we might only have one element or no increasing sequences at all.
'''


class Solution(object):
    def findLengthOfLCIS(self, nums):
        n = len(nums) - 1
        current_length = 1
        max_length = 1

        for i in range(n):
            if nums[i] < nums[i + 1]:
                current_length += 1
                max_length = max(current_length,max_length)
            else:
                current_length = 1
        
        return max_length