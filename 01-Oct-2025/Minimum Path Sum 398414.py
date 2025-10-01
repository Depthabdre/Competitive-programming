# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])


        def inbound(r , c):
            return 0 <= r < m and 0 <= c < n
        
        memo = [[-1] * n for i in range(m)]
        def dp( i , j):
            if i == 0 and j ==0:
                return grid[0][0]
            if memo[i][j] != -1:
                return memo[i][j]
            ans1 , ans2 = float('inf') , float("inf")
            if inbound(i ,j - 1) :
                ans1 = dp(i ,j - 1) + grid[i][j]
            if inbound(i - 1 , j):
                ans2 = dp( i -1 , j) + grid[i][j]
            
            memo[i][j] = min(ans1 , ans2)

            return memo[i][j]
        
        return dp( m -1 , n -1)
        