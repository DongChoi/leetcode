class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force first
        #optimize little by little
        #loop through the array and do a two sum
        #lets sort it
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            right = len(nums) - 1
            left = i + 1
            print(i, left,right)
            resp = self.twoSum(nums, i, left, right)
            if resp:
                for response in resp:
                    if response not in res:
                        res.append(response)
        return res

    def twoSum(self, nums, curr_i, left,right):
        res = []
        while left < right:
            three_nums_added = nums[curr_i] + nums[left] + nums[right]
            if three_nums_added > 0:
                right -= 1
            elif three_nums_added < 0:
                left += 1
            else:
                res.append([nums[curr_i], nums[left], nums[right]])
                left += 1
        return res

