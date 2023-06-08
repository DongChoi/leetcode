class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        res = -1
        while index < len(haystack):
            if (
                haystack[index] == needle[0]
                and haystack[index : (index + len(needle))] == needle
            ):
                res = index

            if res != -1:
                return res
            index += 1
        return res
