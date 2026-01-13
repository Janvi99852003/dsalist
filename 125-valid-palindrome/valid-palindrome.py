class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for ch in s:
            if ch.isalnum():          # keep letters and numbers
                word += ch.lower()   # convert to lowercase

        l = 0
        r = len(word) - 1

        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1

        return True
