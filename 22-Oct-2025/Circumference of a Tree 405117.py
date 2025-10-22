# Problem: Circumference of a Tree - https://codeforces.com/gym/102694/problem/A

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, n, graph):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([(start, 0)])
    farthest_node = start
    max_dist = 0

    while queue:
        node, dist = queue.popleft()
        if dist > max_dist:
            max_dist = dist
            farthest_node = node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))
    return farthest_node, max_dist

def main():
    n = int(input())
    if n == 1:
        print(0)
        return

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

   
    node_a, _ = bfs(1, n, graph)
   
    _, diameter = bfs(node_a, n, graph)

    print(3 * diameter)

if __name__ == "__main__":
    main()
