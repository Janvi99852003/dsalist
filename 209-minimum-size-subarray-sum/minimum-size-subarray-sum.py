class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        s = 0
        c = 0
        min_length = len(nums) + 1
        while r < len(nums):
            s += nums[r]
            while s >= target and l <= r:
                c = r - l + 1
                min_length = min(c, min_length)
                s -= nums[l]
                l += 1
            r += 1
        return 0 if min_length == len(nums) + 1 else min_length
