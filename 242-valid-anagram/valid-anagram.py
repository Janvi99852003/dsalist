class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char_counts=[0]*26
        for i in range(0,len(s)):
            char_counts[ord(s[i])-ord('a')]+=1
            char_counts[ord(t[i])-ord('a')]-=1
        for c in char_counts:
            if c!=0:
                return False
        return True

