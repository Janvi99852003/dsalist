class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_hash = {}
        
        for i in range(len(nums)):
            if nums[i] not in my_hash:
                my_hash[nums[i]] = 1      # fix: key should be nums[i]
            else:
                my_hash[nums[i]] += 1     # fix: increment count
        
        for key in my_hash:
            if my_hash[key] > len(nums) // 2:
                return key
