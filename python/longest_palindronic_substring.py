"""
Given a string s, return the longest 
palindromic substring in s.


#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # the best i can think of is O(n^2)
        res = ""
        resLen = 0
        for i in range(len(s)):
            # odds
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                r += 1
                l -= 1
            # evens
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                r += 1
                l -= 1

        return res
