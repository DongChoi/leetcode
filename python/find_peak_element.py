# NEETCODE SOLUTION


# MY SOLUTION


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = 0
        prev = float("-inf")

        for i in range(0, len(nums)):
            if i == len(nums) - 1 and nums[i] > prev and nums[i] > float("-inf"):
                return i
            if nums[i] > prev and nums[i] > nums[i + 1]:
                return i
            prev = nums[i]

        return res
