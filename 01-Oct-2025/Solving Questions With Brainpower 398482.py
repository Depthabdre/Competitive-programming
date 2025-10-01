# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = [-1 for i in range(len(questions))]
        def dp(index):
            if index >= len(questions):
                return 0
            if memo[index] != -1:
                return memo[index]
            solve = dp(index +  questions[index][1] + 1) + questions[index][0]
            skip = dp(index + 1)

            memo[index] = max(solve , skip)
            return memo[index]
        return dp(0)
        