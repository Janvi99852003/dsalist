class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        my_hash = {}
        for i in range(len(order)):
            my_hash[order[i]] = i
        

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            
            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if my_hash[w1[j]] > my_hash[w2[j]]:
                        return False
                    break  
           
            else: 
                if len(w1) > len(w2):
                    return False
        
        return True