# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        n = len(isWater)
        m = len(isWater[0]) 
        def inbound(row,col):
            return 0 <= row < n and 0 <= col < m 
        zer = []
        maze = [['+' for _ in range(m)] for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    queue.append((i,j))
                    maze[i][j] = 0   
       
        level = 1
        while queue:
            for i in range(len(queue)):
                cur_r, cur_c = queue.popleft()
                for i , j in direction:
                    new_r = cur_r + i
                    new_c = cur_c + j
                   
                    if inbound(new_r,new_c) and maze[new_r][new_c] == '+':
                        print(new_r,new_c)
                        maze[new_r][new_c] = level

                        queue.append((new_r,new_c))
            level += 1
        return maze