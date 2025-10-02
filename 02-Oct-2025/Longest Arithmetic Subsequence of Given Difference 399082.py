# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        limit =  ( 10**4)
        dp = [0 for i in range(3 * (limit) + 2)]
        occur = {}
        print(f"dp at {dp[limit + limit]}")
        for i in range(len(arr)):
            dp[arr[i] + limit] = max(dp[arr[i] + limit] , dp[arr[i] - difference + limit] + 1)
            
            
        return max(dp)

        
            
            
        