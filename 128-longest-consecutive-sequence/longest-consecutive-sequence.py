class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        s=set(nums)
        
        for x in s:
            i=1
            if x-i not in s:
                while x+i in s:
                    i+=1
                longest=max(i,longest)
        return longest