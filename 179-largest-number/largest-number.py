from typing import List
from functools import cmp_to_key   # ← only new import needed

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings (minimal & necessary step)
        strs = [str(num) for num in nums]
        
        # Custom comparator: decide if a should come before b
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1   # a should come first (for descending "greatness")
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        # Sort using the custom comparator
        strs.sort(key=cmp_to_key(compare))
        
        # Handle all-zero case → return "0" instead of "000..."
        if strs[0] == "0":
            return "0"
            
        # Join and return
        return "".join(strs)