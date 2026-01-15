class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = 0
        for i in range(len(nums1)):
            if nums1[i] == 0 and p < n:
                nums1[i] = nums2[p]
                p += 1

        nums1.sort()
