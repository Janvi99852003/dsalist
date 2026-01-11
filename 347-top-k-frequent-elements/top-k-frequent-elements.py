

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash = {}
        for num in nums:               
            if num in my_hash:
                my_hash[num] += 1
            else:
                my_hash[num] = 1
        
       
        sorted_nums = sorted(my_hash, key=my_hash.get, reverse=True)
        
       
        return sorted_nums[:k]