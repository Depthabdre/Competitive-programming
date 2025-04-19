# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        prev = image[sr][sc]
        queue = deque([(sr,sc)])
        dxn = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        visited =set((sr,sc))
        while queue:
            for i in range(len(queue)):
                row , col = queue.popleft()
                image[row][col] = color
                for dx , dy in dxn:
                    new_row = dx + row
                    new_col = dy + col

                    if inbound(new_row,new_col) and (new_row,new_col) not in visited and  image[new_row][new_col] == prev:
                        
                        queue.append((new_row,new_col))
                        visited.add((new_row,new_col))
        return image
        