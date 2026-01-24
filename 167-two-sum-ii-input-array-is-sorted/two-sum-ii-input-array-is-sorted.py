class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_hash={}
        for i in range(0,len(numbers)):
            comp=target-numbers[i]
            if comp in my_hash:
                return [my_hash[comp]+1,i+1]
            else:
                my_hash[numbers[i]]=i
        return []