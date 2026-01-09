class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in my_hash:
                return [my_hash[comp], i]
            my_hash[nums[i]] = i  
        return []