# @leet start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # pointer for nums1
        p1 = m - 1
        # pointer for nums2
        p2 = n - 1
        # sort operation count
        c = 0

        while p1 >= 0 and p2 >= 0:
            if nums2[p2] >= nums1[p1]:
                nums1[m + n - c - 1] = nums2[p2]
                p2 = p2 - 1
            else:
                nums1[m + n - c - 1] = nums1[p1]
                p1 = p1 - 1
            c += 1

        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1


# @leet end

