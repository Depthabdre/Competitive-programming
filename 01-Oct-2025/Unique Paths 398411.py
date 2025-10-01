# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def inbound(r , c):
            return 0 <= r < m and 0 <= c < n
        
        memo = [[-1] * n for i in range(m)]

        def dp( i , j):
            if i == 0 and j ==0:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            ans1 , ans2 = 0 , 0
            if inbound(i ,j - 1):
                ans1 = dp(i ,j - 1)
            if inbound(i - 1 , j):
                ans2 = dp( i -1 , j)
            
            memo[i][j] = ans1 + ans2

            return memo[i][j]
        
        return dp( m -1 , n -1)
            
            
        