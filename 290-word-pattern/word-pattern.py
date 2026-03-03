class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        my_hash = {}
        
        for i in range(len(pattern)):
            if pattern[i] in my_hash:
                if my_hash[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in my_hash.values():
                    return False
                my_hash[pattern[i]] = words[i]
        
        return True