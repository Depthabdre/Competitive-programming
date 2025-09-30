# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = [[-1] * 2 for _ in range(n)]

        def dp(index: int, holding: int) -> int:
            if index == n:
                return 0
            if memo[index][holding] != -1:
                return memo[index][holding]
            if holding == 0:
                ans = max(dp(index + 1, 0), dp(index + 1, 1) - prices[index])
            else:
                ans = max(dp(index + 1, 1), dp(index + 1, 0) + prices[index] - fee)
            memo[index][holding] = ans
            return ans

        return dp(0, 0)
