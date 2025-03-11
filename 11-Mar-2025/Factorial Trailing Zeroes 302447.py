# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5 :
            return 0
       
        count = self.trailingZeroes(n//5) + n//5

        return count
