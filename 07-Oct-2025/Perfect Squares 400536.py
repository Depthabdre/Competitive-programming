# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for index in range(1 , n+1): 
            if sqrt(index) == int(sqrt(index)):
                nums.append(index)

        memo = [-1 for i in range(n + 1)]

        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float("inf")
            if memo[rem] != -1:
                return memo[rem]
            ans = float('inf')
            for perfectNum in nums:
                temp = dp(rem - perfectNum) + 1
                ans = min(ans , temp)
            memo[rem] = ans
            return ans
        
        return dp(n)

        