'''

414. Third Maximum Number
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.


To solve this problem, I initially thought that I could simply return the last element of the list. 
However, I later realized that I need to find the distinct third maximum number in the array. 
To do this, I should first remove duplicates, then sort the list in decreasing order. 
If the length of the resulting list is 3 or more, I'll return the third element. If it has fewer than 3 elements, I'll return the first element.
'''

class Solution():
    def thirdMax(nums):
        n = list(set(nums)) 

        n.sort(reverse=True)

        if len(n) >= 3:
            return (nums[2])
        else:
            return (nums[0])