class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_hash = {}
        for i in range(len(nums)):
            if nums[i] in my_hash:
                if abs(i - my_hash[nums[i]]) <= k:
                    return True
            my_hash[nums[i]] = i  # Always update to the latest index
        return False