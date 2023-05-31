"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:

#Input: s = "ababcbacadefegdehijhklij"
#Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

#Input: s = "eccbbbbdec"
#Output: [10]

"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        end = 0
        size = 0
        letter_counter = self.hash_letters(s)

        print(letter_counter)
        for i, letter in enumerate(s):
            size += 1
            end = max(end, letter_counter[letter])
            if i == end:
                res.append(size)
                size = 0

        return res

    def hash_letters(self, s):
        letter_counter = {}
        for i, letter in enumerate(s):
            letter_counter[letter] = i
        return letter_counter
