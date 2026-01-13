class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        long = 0
        maxlong = 0

        while r < len(s):
            if s[r] not in s[l:r]:
                long += 1
                maxlong = max(maxlong, long)
                r += 1
            else:
                l += 1
                r = l
                long = 0

        return maxlong
