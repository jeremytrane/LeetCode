class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, maxProfit = prices[0], 0

        for i in range(len(prices)):
            buy = min(buy, prices[i])
            maxProfit = max(maxProfit, prices[i] - buy)
        return maxProfit