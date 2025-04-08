# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        stack = []
        group1 = set()
        group2 = set()

        while graph:
            if not stack:
                seed = next(iter(graph))
                stack.append(seed)
                if seed not in group1 and seed not in group2:
                    group1.add(seed)
            
            node = stack.pop()
            for neighbor in graph.get(node, []):
                if node in group1:
                    if neighbor in group1:
                        return False
                    if neighbor not in group2:
                        group2.add(neighbor)
                        stack.append(neighbor)
                else:
                    if neighbor in group2:
                        return False
                    if neighbor not in group1:
                        group1.add(neighbor)
                        stack.append(neighbor)
            
            if node in graph:
                del graph[node]
        
        return True
