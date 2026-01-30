from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        l = n
        r = -1
        
        max_so_far = nums[0]
        for i in range(1, n):
            if nums[i] >= max_so_far:
                max_so_far = nums[i]
            else:
                r = i
        
        min_so_far = nums[-1]
        for i in range(n-2, -1, -1):
            if nums[i] <= min_so_far:
                min_so_far = nums[i]
            else:
                l = i
        
        if r == -1:
            return 0
            
        return r - l + 1