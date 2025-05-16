# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find the common prefix
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Shift left to restore common bits
        return left << shift
