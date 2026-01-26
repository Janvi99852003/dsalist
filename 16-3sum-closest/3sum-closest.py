class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        diff = abs(target - res)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(target - s) < diff:
                    diff = abs(target - s)
                    res = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s

        return res
