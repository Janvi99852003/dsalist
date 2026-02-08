class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        curr_sum = sum(nums[:k])
        max_sum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[l]
            if curr_sum > max_sum:
                max_sum = curr_sum
            l += 1
        
        return max_sum / k