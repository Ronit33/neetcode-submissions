class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        l = 0
        r = l + 1

        while l < r and r < n:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        
        return max_profit


