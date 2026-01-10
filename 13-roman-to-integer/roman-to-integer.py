class Solution:
    def romanToInt(self, s: str) -> int:
        my_hash={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        r=0
        for i in range(0,len(s)):
            if (i+1<len(s) and my_hash[s[i]]<my_hash[s[i+1]]):
                r-=my_hash[s[i]]
            else:
                r+=my_hash[s[i]]
        return r