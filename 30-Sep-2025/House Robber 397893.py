# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dp(curr):
            if curr == len(nums) - 1:
                return nums[len(nums) - 1]
            if curr >= len(nums):
                return 0
            if curr in memo:
                return memo[curr]
            steal = max(nums[curr] + dp(curr + 2) , nums[curr + 1] +  dp(curr + 3))

            memo[curr] = steal
            return steal
        return dp(0)
        