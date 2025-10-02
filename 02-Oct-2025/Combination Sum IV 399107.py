# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}
        def dp (curr_sum):
            if curr_sum == target:
                return 1
            if curr_sum > target:
                return 0
            if curr_sum in memo:
                return memo[curr_sum]
            ans = 0
            for num in nums:
                ans += dp(curr_sum + num)
            memo[curr_sum] = ans
            return ans
        return dp(0)
        