class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}
        k = 0

        for x in nums:
            freq[x] = freq.get(x, 0) + 1
            if freq[x] <= 2:
                nums[k] = x
                k += 1

        return k
