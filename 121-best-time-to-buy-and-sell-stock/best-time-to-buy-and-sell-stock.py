class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        maxp=0
        l=0
        r=0
        while r<len(prices):

            if prices[l]>prices[r]:
                l=r
                r+=1
            else:
            
                profit=prices[r]-prices[l]
                maxp=max(maxp,profit)
                r+=1
        return maxp
            