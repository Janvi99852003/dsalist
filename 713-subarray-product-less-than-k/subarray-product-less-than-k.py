class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        c = 0
        s = 1  
        while r < len(nums):
            s *= nums[r]  
            while s >= k and l <= r:
                s //= nums[l]  
                l += 1
            c += r - l + 1  
            r += 1
        return c
