# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
      
        if total % 2 != 0:
            return False
        memo = [[-1] * total for i in range(len(nums))]
        target = total // 2
        
        def dp(curr , curr_sum):

            if curr_sum == target:
                return True
            if curr_sum > target:
                return False

            if curr >= len(nums):
                return False
            if memo[curr][curr_sum] != -1:
                return memo[curr][curr_sum]

          
            take = dp( curr + 1 , curr_sum + nums[curr])
            notake = dp( curr + 1 , curr_sum )

            memo[curr][curr_sum] =  take or  notake 

            return  memo[curr][curr_sum]
        
        return dp(0 , 0)

