# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        n = 26  
        
        
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
      
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
       
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
       
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            s = ord(s_char) - ord('a')
            t = ord(t_char) - ord('a')
            if dist[s][t] == INF:
                return -1 
            total_cost += dist[s][t]
        
        return total_cost
        