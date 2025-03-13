# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        tf = [True]*n
        count = n
        i = 0
        step = k-1
        while count > 1:
            if step > 0 and tf[i%n] == 1:
                step -=1
            elif step == 0 and tf[i%n] == 1:
                tf[i%n] = 0
                count -=1
                step = k-1
            i += 1
        for i in range(n):
            if tf[i] == 1:
                return i+1