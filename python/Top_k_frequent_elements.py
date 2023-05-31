class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency counter and go off the list of k most elements

        counter = self.f_counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        buckets = self.put_numbers_in_buckets(counter, buckets)
        res = []
        # for n, c in counter.items():
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

    def put_numbers_in_buckets(self, counter, buckets):
        for n, c in counter.items():
            buckets[c].append(n)
        return buckets

    def f_counter(self, nums):
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        return counter
