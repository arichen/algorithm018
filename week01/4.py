class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return

        q = len(nums1) - 1
        p1, p2 = m - 1, n - 1

        while p2 >= 0:
            if p1 < 0 or nums2[p2] >= nums1[p1]:
                nums1[q] = nums2[p2]
                p2 -= 1
                q -= 1
            else:
                nums1[q], nums1[p1] = nums1[p1], nums1[q]
                q -= 1
                p1 -= 1