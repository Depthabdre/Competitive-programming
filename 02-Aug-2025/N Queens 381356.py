# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.answer = []

        def backtrack(row, queensPosition):
            if row == n:
               
                board = []
                for _, col in sorted(queensPosition):
                    row_str = ['.'] * n
                    row_str[col] = 'Q'
                    board.append(''.join(row_str))
                self.answer.append(board)
                return

            for col in range(n):
                for r, c in queensPosition:
                    if c == col or abs(r - row) == abs(c - col):
                        break
                else:
                    queensPosition.append((row, col))
                    backtrack(row + 1, queensPosition)
                    queensPosition.pop()

        backtrack(0, [])
        return self.answer
