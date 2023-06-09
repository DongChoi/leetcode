class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """I will need to revisit this because even with neetcode I had a hard
        time understanding the concept towards the end. I kind of get it but not
        completely.
        """

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2  # pointer A
            j = half - i - 2  # pointer for B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        # # this is O(m+n) but we need O(log (m+n))
        # combined = []

        # while nums1 or nums2:
        #     if nums1 and not nums2:
        #         combined.append(nums1.pop(0))
        #     elif not nums1 and nums2:
        #         combined.append(nums2.pop(0))
        #     elif nums1[0] <= nums2[0]:
        #         combined.append(nums1.pop(0))
        #     else:
        #         combined.append(nums2.pop(0))
        # print(combined)
        # if len(combined) % 2 != 0:
        #     return combined[len(combined)//2]
        # else:
        #     return (combined[(len(combined)//2)-1] + combined[(len(combined)//2)]) / 2

        # # this is O((n+n) log m+n))
        # nums = nums1 + nums2
        # print(nums)
        # nums.sort()
        # res =  nums[len(nums)//2]
        # if len(nums) % 2 != 0:
        #     return res
        # else:
        #     return (nums[(len(nums)//2)-1] + nums[(len(nums)//2)]) / 2
