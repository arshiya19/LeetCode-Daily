'''
2351. First Letter to Appear Twice

Input: s = "abccbaacz"
Output: "c"

Using set here to track the number of elements, if there is already a character in set then i am returning that character
'''

class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()

        for char in s:
            if char in seen:
                return char
            seen.add(char)

s = "abccbaacz"
solution = Solution()
ans = solution.repeatedCharacter(s)
print(ans)