# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if not inbound(row, col) or visited[row][col] or grid[row][col] == 0:
                return 0

            visited[row][col] = True
            area = 1  

            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j))

        return max_area
