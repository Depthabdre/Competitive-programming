# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        ans = [0] * (rowIndex + 1)
        ans[0] = 1
        ans[-1] = 1
        prev = self.getRow(rowIndex - 1)

        for i in range(1, rowIndex):  
            ans[i] = prev[i] + prev[i - 1]
        
        return ans
