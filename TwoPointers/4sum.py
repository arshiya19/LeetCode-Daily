
'''

Initially, the mistake I made while working on the 4Sum problem was blindly initializing the four pointers and trying to move them when the sum equaled the target. This approach failed because it wasn't a brute-force solution, nor was it optimal.

 After some attempts, I searched on ChatGPT and learned that we need to fix the first two pointers, then use the other two, adjusting their positions based on the target requirements.

The time complexity is O(n^3) because I am sorting the array first, which takes O(nlogn), and the nested loops will cost O(n^3)
in total. Hence, the overall time complexity is O(n^3)
 
'''
class Solution(object):
    def fourSum(self,nums,target):
        nums.sort()
        n = len(nums)
        res = []

        for a in range(n-3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue 

            for b in range(a+1,n-2):

                if b > a + 1 and nums[b] == nums[b-1]:
                    continue 

                left = b + 1
                right = n - 1

                while left < right:

                    curr_sum = nums[a] + nums[b] + nums[left] + nums[right]

                    if curr_sum == target:
                        res.append([nums[a],nums[b],nums[left],nums[right]])
                        left += 1
                        right -= 1
                    
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                        
                    elif curr_sum < target :
                        left += 1
                    else:
                        right -= 1
        
        return res 


nums = [1,0,-1,0,-2,2]
target = 0
solution = Solution()
ans = solution.fourSum(nums,target)
print(ans)