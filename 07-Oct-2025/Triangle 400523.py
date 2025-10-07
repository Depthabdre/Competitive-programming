# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        memo = {}
        def dp(prev , index):
            if index >= len(triangle):
                return 0
            if (prev , index) in memo:
                return memo[(prev , index)]

            take = dp(prev , index + 1) + triangle[index][prev]
            take2 = dp(prev + 1 , index + 1) + triangle[index][prev+1]

            memo[(prev , index)] = min(take , take2)
            return  min(take , take2)
        return dp(0 , 1) + triangle[0][0]
        