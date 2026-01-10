class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash = {}
        for i in range(len(strs)):
            sorted_words = ''.join(sorted(strs[i]))
            if sorted_words in my_hash:
                my_hash[sorted_words].append(strs[i])
            else:
                my_hash[sorted_words] = [strs[i]]
        return list(my_hash.values())
