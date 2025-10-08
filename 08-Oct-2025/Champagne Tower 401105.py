# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured < 1:
            return 0
        def inbound(r , c):
            return 0 <= r and  0 <= c <= r
        dp = []
        for i in range(100):
            temp = []
            for j in range(i+1):
                temp.append(0)
            dp.append(temp)
        dp[0][0] = poured
        print(f"poss is {dp}")
        
        for i in range(1, 100):
            for j in range(i+1):
                if j - 1 >= 0 and dp[i-1][j-1] > 1:
                    dp[i][j] += (dp[i-1][j-1] - 1) / 2
                if j < i and dp[i-1][j] > 1:
                    dp[i][j] += (dp[i-1][j] - 1) / 2

        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1

        
        