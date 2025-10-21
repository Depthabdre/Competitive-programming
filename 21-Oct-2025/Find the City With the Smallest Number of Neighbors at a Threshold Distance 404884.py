# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

def floyd_warshall(n, edges):
    
    INF = float('inf')

    dist = [[INF] * n for _ in range(n)]

    
    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)  
        dist[v][u] = min(dist[v][u], w)  

   
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = floyd_warshall(n, edges)
        answer = []

        for i in range(len(matrix)):
            ans = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] <= distanceThreshold:
                    ans += 1
            answer.append(ans)
        mins = min(answer)
        for i in range(len(answer) - 1 , -1 , -1):
            if answer[i] == mins:
                return i


        