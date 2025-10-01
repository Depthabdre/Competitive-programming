# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dp(index , curr_sum):
            if index >= len(nums) and curr_sum == target:
                return 1
            if  index >= len(nums) and curr_sum != target:
                return 0
            if (index , curr_sum) in memo:
                return memo[(index , curr_sum)]
            
            add = dp(index + 1 , curr_sum + nums[index])
            subtract = dp(index + 1 , curr_sum - nums[index])

            memo[(index , curr_sum)] = add + subtract
            return add + subtract
        return dp(0 , 0)
        