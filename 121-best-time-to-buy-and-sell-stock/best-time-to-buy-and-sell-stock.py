class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = prices[0], 0
        for price in prices:
            if price > sell:
                sell = price
            if buy > price:
                buy = price
                sell = price
            max_profit = max(max_profit, sell - buy)
        
        return max_profit


