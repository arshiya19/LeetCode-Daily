'''

Two sum problem using Hashmaps

As you iterate through the list of numbers (nums), calculate the complement as target - num. Check if this complement is already present in the complement_map (which keeps track of numbers seen so far along with their indices). 
If the complement is found in the map, return the indices of the current number and the complement. If the complement is not found, add the current number along with its index to the complement_map. Continue this process until a solution is found.

input : nums = [2,7,11,15], target = 9
output : [0,1]

'''

class Solution(object):
    def twoSum(self,nums,target):
        seen_map = {}

        for i,num in enumerate(nums):
            complement = target - num

            if complement in seen_map:
                return [seen_map[complement],i]
            else:
                seen_map[num] = i 
        
        return []

nums = [2,7,11,15] 
target = 13
solution = Solution()
ans = solution.twoSum(nums,target)
print(ans) 

