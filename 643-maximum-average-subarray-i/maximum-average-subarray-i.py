class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current=sum(nums[:k])
        best=current
        for i in range(k, len(nums)):
            current = current - nums[i - k] + nums[i]
            if current > best:
                best = current
        
        return best / k
