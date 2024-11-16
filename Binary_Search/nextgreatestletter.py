'''

744. Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

'''

class Solution(object):
    def nextGreatestLetter(self, letters, target):

        # s1_count = [0] * 26
        
        # for letter in letters:
        #     s1_count[ord(letter) - ord('a')] += 1
        
        # target_index = ord(target) - ord('a')
        # for i in range(len(s1_count)):
        #     if s1_count[i] > 0 and i > target_index:
        #         return chr(i + ord('a')) 

        # for i in range(len(s1_count)):
        #     if s1_count[i] > 0:
        #         return chr(i + ord('a'))


        '''BINARY SEACRH LOGIC'''

        left = 0
        right = len(letters) - 1

        while left < right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # if left == len(letters):
        #     return letters[0]
        # else:
        #     return letters[left]
        
        return letters[left % len(letters)]

