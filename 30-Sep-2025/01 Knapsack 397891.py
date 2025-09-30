# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        memo = [[-1 for _ in range(W + 1)] for _ in range(n)]

        def dp(curr_indx, rem_weight):
           
            if curr_indx >= n:
                return 0
            if rem_weight <= 0:
                return 0

           
            if memo[curr_indx][rem_weight] != -1:
                return memo[curr_indx][rem_weight]

           
            take = 0
            if rem_weight >= wt[curr_indx]:
                take = dp(curr_indx + 1, rem_weight - wt[curr_indx]) + val[curr_indx]

           
            no_take = dp(curr_indx + 1, rem_weight)

           
            memo[curr_indx][rem_weight] = max(take, no_take)
            return memo[curr_indx][rem_weight]

        return dp(0, W)
