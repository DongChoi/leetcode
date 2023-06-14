"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice. 
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        no_remainders = []
        s_len = len(s)
        if len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False

        for digit in range(1, len(s) // 2 + 1):
            if s_len % digit == 0:
                no_remainders.append(digit)
        print(no_remainders)
        # create snapshot and see if it repeats all the way to the end

        for window_size in no_remainders:
            sub_str = s[:window_size]
            res = "False"
            for i in range(0, len(s), window_size):
                print(sub_str, s[i : i + window_size], i)
                if sub_str == s[i : i + window_size]:
                    res = "True"
                else:
                    res = "False"
                    break
            print(res)
            if res == "True":
                return True

        return False
