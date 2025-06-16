# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        memo = {}  # (r, c) -> longest increasing path from (r, c)

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            max_len = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

            memo[(r, c)] = max_len
            return max_len

        answer = 0
        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r, c))

        return answer
