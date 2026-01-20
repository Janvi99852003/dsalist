class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        
        for i in range(n):
            # Odd length palindromes (center at i)
            ans += self.checkpalin(s, i, i)
            # Even length palindromes (center between i and i+1)
            ans += self.checkpalin(s, i, i+1)
        
        return ans
    
    def checkpalin(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # Every time we find a valid palindrome, count it
            count += 1
            left -= 1
            right += 1
        return count