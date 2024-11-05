'''
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
       
        # FIRST APPROACH
        # if n % 2 == 1:
        #     return True
        # else:
        #     return False

        #/* SECOND APPROACH */
        # ones = zeroes = 0

        # for num in flowerbed:
        #     if num == 0:
        #         zeroes += 1
        #     else:
        #         ones += 1

        # total = zeroes - ones

        # if total >= n:
        #     return True
        # else:
        #     return False

        
        # THIRD APPROACH

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

            
        return n <= 0

