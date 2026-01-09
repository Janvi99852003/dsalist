class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_hash={}
        for i in range(0,len(nums)):
            if nums[i] in my_hash:
                return True
            else:
                my_hash[nums[i]]=i
        return False