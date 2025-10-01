# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = [-1 for i in range(len(cost))]
        def dp(index):
            if index >= len(cost):
                return 0
            if  memo[index] != -1:
                return memo[index]
            oneStep = dp(index + 1) + cost[index]
            twoStep = dp(index + 2) + cost[index]
            ans = min(oneStep , twoStep)
            memo[index] = ans

            return ans
        return min(dp(0) , dp(1))
        