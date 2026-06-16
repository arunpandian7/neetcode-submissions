class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0

        for sell in prices[1:]:
            profit = sell - min_buy
            max_profit = max(profit, max_profit)

            if sell < min_buy:
                min_buy = sell
            
        return max_profit
