from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       

        s = strs          
        f = ""
        r = 0

        while r < len(min(s)):
            ch = s[0][r]
            for word in s:
                if word[r] != ch:
                    return f
            f += ch
            r += 1

        return f
