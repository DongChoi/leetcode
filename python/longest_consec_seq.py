# could not sort due to O(n) restriction.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 0
        counter = 0
        hash_map = self.hash_nums(nums)
        switch = True
        for num in nums:
            # check if it is not a starting value to skip
            if num - 1 in hash_map:
                continue
            # if starting value, iterate until no continued found
            else:
                switch = True
                line = num
                while switch:
                    counter += 1
                    if line + 1 in hash_map:
                        line += 1
                    else:
                        switch = False
                res = max(res, counter)
                counter = 0
        return res

    def hash_nums(self, nums):
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = True
        return hash_map
