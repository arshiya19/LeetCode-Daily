'''
Geeks for Geeks 

Min and Max in Array
Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return an array that contains two elements the first one will be a minimum element and the second will be a maximum of an array.

Examples:

Input: arr = [3, 2, 1, 56, 10000, 167]
Output: 1 10000
Explanation: minimum and maximum elements of array are 1 and 10000.
Input: arr = [1, 345, 234, 21, 56789]
Output: 1 56789
Explanation: minimum and maximum element of array are 1 and 56789.
'''

class Solution:
    def get_min_max(self, arr):
        mini = arr[0]
        maxi = arr[0]
        
        for num in arr:
            if num < mini:
                mini = num
            
            elif num > maxi:
                maxi = num
        
        return mini,maxi