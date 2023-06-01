"""easy but had a hard time T^T"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = nums[0]
        res = 1
        l = 1
        r = len(nums)
        while l < r:
            if curr == nums[l]:
                print(curr, nums[l])
                nums.pop(l)

                r -= 1
            else:
                curr = nums[l]
                l += 1
                res += 1
        return res
