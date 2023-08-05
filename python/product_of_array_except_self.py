class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pre = 1
        post = 1

        for i in range(len(nums)):
            if i == 0:
                res[i] = 1
            res[i] = pre
            pre = pre * nums[i]
        print(res)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                res[i] = res[i] * 1
                post = post * nums[i]
                continue
            res[i] = post * res[i]
            post = post * nums[i]
        return res
