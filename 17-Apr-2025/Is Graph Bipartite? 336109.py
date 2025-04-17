# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  
        
        for node in range(len(graph)):
            if node not in color:
                queue = deque([node])
                color[node] = 0  
                
                while queue:
                    current = queue.popleft()
                    for neighbor in graph[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]  
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False  
                            
        return True
