# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = [[-1] * 2 for j in range(len(prices))]
        def dp(index , hold):

            if index >= len(prices):
                return 0
            if memo[index][hold] != -1:
                return memo[index][hold]
            ans = 0
            if hold:
                sell = dp(index + 2 , 0) + prices[index]
                skip = dp(index + 1 , 1)
                ans = max(sell , skip)
            else:
                buy = dp(index + 1 , 1) - prices[index]
                skip = dp(index + 1 , 0)
                ans = max(buy , skip)
            memo[index][hold] = ans
            return ans
        return dp(0 , 0)
        