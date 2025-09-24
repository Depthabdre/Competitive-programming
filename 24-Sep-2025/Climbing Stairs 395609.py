# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        total = 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        prev = 1
        now = 2
        for i in range(2,n):
            total = prev + now
            prev = now
            now = total
        return total

       