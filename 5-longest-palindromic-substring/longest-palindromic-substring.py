class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        n = len(s)

        for i in range(n):
            temp = self.checkpalin(s, i, i)
            if len(temp) > len(ans):
                ans = temp

            temp = self.checkpalin(s, i, i+1)
            if len(temp) > len(ans):
                ans = temp

        return ans

    def checkpalin(self, s: str, left: int, right: int) -> str:
        max_palin = ""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if len(s[left:right+1]) > len(max_palin):
                max_palin = s[left:right+1]

            left -= 1
            right += 1

        return max_palin
