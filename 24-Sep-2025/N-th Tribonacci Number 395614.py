# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:

        memo = [-1] * (n + 1) 

        def dp(i):

            if i == 0 or i == 1:
                return i
            elif i == 2:
                return 1
            elif memo[i] != -1:
                return memo[i]
            
            ans = dp(i - 1) + dp(i - 2) + dp(i - 3)

            memo[i] = ans
            return ans
        return dp(n)
        