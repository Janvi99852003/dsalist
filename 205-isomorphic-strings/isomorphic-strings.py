class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        my_hash = {}
        for i in range(len(s)):
            if s[i] in my_hash:
                if my_hash[s[i]] != t[i]:   # fixed here
                    return False
            else:   # added this else for outer if
                if t[i] in my_hash.values():   # fixed spelling
                    return False
                my_hash[s[i]] = t[i]
        return True