"""
383. Ransom Note
Easy
4K
423
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


# I think another solution is to sort both stringss and loop through the ransom note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_note_hash = self.f_counter(ransomNote)
        m_hash = self.f_counter(magazine)
        for key, value in r_note_hash.items():
            if key in m_hash and m_hash[key] >= r_note_hash[key]:
                continue
            else:
                return False
        return True

    def f_counter(self, str):
        counter = {}
        for letter in str:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1

        return counter
