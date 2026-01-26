class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        pos = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] * nums[l]
                l += 1
            else:
                res[pos] = nums[r] * nums[r]
                r -= 1
            pos -= 1

        return res
