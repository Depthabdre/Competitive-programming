# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dp(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index in memo:
                return memo[index]
            
         
            ans = dp(index + 1)
            
          
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                ans += dp(index + 2)
            
            memo[index] = ans
            return ans
        
        return dp(0)
