class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        c = 0
        st = s[:3]

        if len(set(st)) == 3:
            c += 1

        for i in range(3, len(s)):
            st = st[1:] + s[i]
            if len(set(st)) == 3:
                c += 1
            l += 1

        return c
