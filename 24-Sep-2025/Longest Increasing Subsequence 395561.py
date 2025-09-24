# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def longest_increasing_subsequence(arr):
            n = len(arr)
            if n == 0:
                return 0

           
            dp = [1] * n  

            
            for i in range(1, n):
                for j in range(i):
                    if arr[j] < arr[i]:
                        dp[i] = max(dp[i], dp[j] + 1)

           
            return max(dp)
        return longest_increasing_subsequence(nums)