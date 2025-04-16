# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_fruit = sum(cell != 0 for row in grid for cell in row)
        que = deque()
        if total_fruit == 0:
            return 0
        

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    que.append((i, j))  
        count = len(que)
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        minute_count = 0
        def inbound(row,col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                return True
            return False
       
        while que:
            level_iter = len(que)
            if count == total_fruit:
                return minute_count
            

            for i in range(len(que)):
                row , col = que.popleft()
                for dx , dy in direction:
                    new_row = row + dx
                    new_col = col + dy
                    if inbound(new_row,new_col):
                        if grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 2
                            count += 1
                            que.append((new_row,new_col))
            minute_count += 1
            
        return -1
            
        