# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        validchecker = defaultdict(bool)

        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))
        def dfs(row, col):
            is_check = False
            # base case
            visited[row][col] = True

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and not visited[new_row][new_col] and board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)
                    is_check = True
            if not is_check:
                is_valid = True
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if not inbound(new_row, new_col):
                        is_valid = False
                        break
                if is_valid:
                    validchecker[(row,col)] = True
                else:
                    validchecker[(row,col)] = False
            else:
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if not inbound(new_row, new_col):
                        validchecker[(row,col)] = False
                        break
                    else :
                        validchecker[(row,col)] = True
              
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == 'O':
                    
                    dfs(i,j)
                    is_check = True
                    print(validchecker)
                    for key in validchecker:
                        if not validchecker[key]:
                            is_check = False
                            break
                    if is_check:
                        for key in validchecker:
                            rows = list(key)
                            board[rows[0]][rows[1]] = 'X'
                    validchecker = defaultdict(bool)


