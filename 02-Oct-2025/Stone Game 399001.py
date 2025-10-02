# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = [[-inf] * len(piles) for i in range(len(piles))]
        def dp(l , r):
            if l > r:
                return 0
            if memo[l][r] != -inf:
                return memo[l][r]
            takeAtLeft = piles[l] - dp(l + 1 , r) 
            takeAtRight =  piles[r] - dp(l , r -1) 
            ans = max(takeAtLeft , takeAtRight)
            memo[l][r] = ans
            return ans
        if dp(0 , len(piles) -1) > 0:
            return True
        else:
            return False
        