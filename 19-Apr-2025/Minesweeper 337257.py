# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        dxn = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        def inbound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        queue = deque([(click[0],click[1])])

        visited = set()
        visited.add((click[0],click[1]))
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board 


        while queue:

            for i in range(len(queue)):
                row , col = queue.popleft()
                count = 0
                for dx , dy in dxn:
                    new_row = row + dx 
                    new_col = col + dy
                    if inbound( new_row , new_col ) and (new_row , new_col ) not in visited:
                        if board[new_row][new_col] == "M":
                            count += 1
                if count != 0:
                    board[row][col] = str(count)
                else:
                    for dx , dy in dxn:
                        new_row = row + dx 
                        new_col = col + dy
                        if inbound( new_row , new_col ) and (new_row , new_col ) not in visited:
                            queue.append((new_row , new_col))
                            visited.add((new_row , new_col))
                    board[row][col] = "B"
        return board
            





        