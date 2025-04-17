# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dxn = [(0,1),(1,0),(-1,0),(0,-1)]
        tot_row = len(mat)
        tot_col = len(mat[0])
        
        def inbound(row,col):
            return 0 <= row < tot_row and 0 <= col < tot_col

        answer = [[-1 for _ in range(tot_col)] for _ in range(tot_row)]
        queue = deque()

       
        for i in range(tot_row):
            for j in range(tot_col):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    answer[i][j] = 0

       
        while queue:
            row, col = queue.popleft()
            for dx, dy in dxn:
                new_r, new_c = row + dx, col + dy
                if inbound(new_r, new_c) and answer[new_r][new_c] == -1:
                    answer[new_r][new_c] = answer[row][col] + 1
                    queue.append((new_r, new_c))
        
        return answer
