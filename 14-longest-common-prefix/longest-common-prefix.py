from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       

                
        f = ""
        r = 0

        while r < len(min(strs)):
            ch = strs[0][r]
            for word in strs:
                if word[r] != ch:
                    return f
            f += ch
            r += 1

        return f
