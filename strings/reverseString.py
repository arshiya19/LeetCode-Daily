'''
Geeks for Geeks

You are given a string s, and your task is to reverse the string.

Examples:

Input: s = "Geeks"
Output: "skeeG"
Input: s = "for"
Output: "rof"
Input: s = "a"
Output: "a"

'''

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        i = 0 
        j = len(s) - 1
        s_list = list(s)
        
        while i < j:
            s_list[i],s_list[j] = s_list[j],s_list[i]
            i += 1
            j -= 1
        
        swapp_s = ''.join(s_list)
        
        return swapp_s