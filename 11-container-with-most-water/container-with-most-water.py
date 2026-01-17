class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            w = r - l              # FIXED
            h = min(height[l], height[r])
            a = w * h
            res = max(res, a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
