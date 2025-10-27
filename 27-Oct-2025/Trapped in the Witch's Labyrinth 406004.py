# Problem: Trapped in the Witch's Labyrinth - https://codeforces.com/problemset/problem/2034/C

from collections import deque

def count_loop_cells():
    test_cases = int(input())
    results = []

    for _ in range(test_cases):
        rows, cols = map(int, input().split())
        maze = [input().strip() for _ in range(rows)]

        grid = [['-'] * (cols + 2)]
        for row in maze:
            grid.append(['-'] + list(row) + ['-'])
        grid.append(['-'] * (cols + 2))

        reversed_graph = [[[] for _ in range(cols + 2)] for _ in range(rows + 2)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if grid[i][j] == 'U':
                    reversed_graph[i-1][j].append((i, j))
                elif grid[i][j] == 'D':
                    reversed_graph[i+1][j].append((i, j))
                elif grid[i][j] == 'L':
                    reversed_graph[i][j-1].append((i, j))
                elif grid[i][j] == 'R':
                    reversed_graph[i][j+1].append((i, j))

        can_exit = [[False] * (cols + 2) for _ in range(rows + 2)]
        queue = deque()

        for j in range(cols + 2):
            can_exit[0][j] = True
            queue.append((0, j))
            can_exit[rows+1][j] = True
            queue.append((rows+1, j))
        for i in range(1, rows + 1):
            can_exit[i][0] = True
            queue.append((i, 0))
            can_exit[i][cols+1] = True
            queue.append((i, cols+1))

        while queue:
            r, c = queue.popleft()
            for nr, nc in reversed_graph[r][c]:
                if not can_exit[nr][nc]:
                    can_exit[nr][nc] = True
                    queue.append((nr, nc))

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if grid[i][j] == '?':
                    if can_exit[i-1][j] and can_exit[i+1][j] and can_exit[i][j-1] and can_exit[i][j+1]:
                        can_exit[i][j] = True

        loop_cells_count = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if not can_exit[i][j]:
                    loop_cells_count += 1

        results.append(loop_cells_count)

    for res in results:
        print(res)

count_loop_cells()
