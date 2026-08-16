class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprofit = 0
        for price in prices:
            profit = price - minprice
            minprice = min(price, minprice)
            maxprofit = max(profit, maxprofit)
        
        return maxprofit
        