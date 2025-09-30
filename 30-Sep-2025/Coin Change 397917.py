# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0

        for amt in range(1, amount + 1):
            ans = inf
            for coin in coins:
                if amt - coin >= 0:
                    ans = min ( ans , dp[amt - coin] + 1)
            dp[amt] = ans
                
        return dp[amount] if dp[amount] != inf else -1
        