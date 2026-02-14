class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_length = 0
        w = ""
        while r < len(s):
            if s[r] not in w:
                w += s[r]
                max_length = max(len(w), max_length)
                r += 1
            else:
                w = w[1:]
                l += 1
        return max_length
