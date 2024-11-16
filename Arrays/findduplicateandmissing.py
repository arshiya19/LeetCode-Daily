'''
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
'''

# MY initial approach -  not in an optimized way

nums = [3, 1, 2, 5, 3]

n = len(nums)
rep = []
miss = []

num_set = set()

for i in range(n):
  if nums[i] not in num_set:
    num_set.add(nums[i])
  else:
    rep.append(nums[i])

# print(num_set)
for num in range(min(num_set),max(num_set)):
  if num not in num_set:
    miss.append(num)

print(rep + miss)

nums = [3, 1, 2, 5, 3]


n = len(nums)
duplicate = -1
missing = -1

#step 1: finding the duplicates and marking them 
for num in nums:
  index = abs(num) - 1
  if nums[index] < 0:
    duplicate = abs(num)
  else:
    nums[index] = -nums[index]

for i in range(n):
  if nums[i] > 0:
    missing = i + 1
    break
print(duplicate,missing)
