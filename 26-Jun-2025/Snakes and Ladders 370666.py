# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coords(s):
            # Converts square number to (row, col) on the board
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else (n - 1 - rem)
            return row, col

        visited = set()
        queue = deque()
        queue.append((1, 0))  # (square, moves)

        while queue:
            s, moves = queue.popleft()
            for i in range(1, 7):
                next_s = s + i
                if next_s > n * n:
                    continue
                r, c = get_coords(next_s)
                if board[r][c] != -1:
                    next_s = board[r][c]

                if next_s == n * n:
                    return moves + 1
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s, moves + 1))
        return -1
