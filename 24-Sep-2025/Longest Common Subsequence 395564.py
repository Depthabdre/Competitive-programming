# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)
        memo = [[-1 for _ in range(n)] for _ in range(m)] 

        def dp ( currM , currN):

            if currM < 0 or currN < 0:
                return 0

            if memo[currM][currN] != -1:
                return  memo[currM][currN]
            
            if text1[currM] == text2[currN]:

                memo[currM][currN] = 1 + dp ( currM -1 , currN - 1)
            else:
                memo[currM][currN] = max (dp (currM , currN - 1) , dp ( currM -1 , currN))
            
            return memo[currM][currN]
        
        return dp(m - 1 , n - 1)
        