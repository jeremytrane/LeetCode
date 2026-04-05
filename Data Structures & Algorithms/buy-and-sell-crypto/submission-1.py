class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, max_profit = float("inf"), 0
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            max_profit = max(max_profit, prices[i]-buy)
        return max_profit