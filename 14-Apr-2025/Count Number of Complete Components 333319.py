# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        total = 0

        def dfs(node, component_nodes):
            visited.add(node)
            component_nodes.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component_nodes)

        for node in range(n):
            if node not in visited:
                component_nodes = []
                dfs(node, component_nodes)
                edge_count = 0
                for u in component_nodes:
                    edge_count += len(graph[u])
                edge_count //= 2
                num_nodes = len(component_nodes)
                if edge_count == num_nodes * (num_nodes - 1) // 2:
                    total += 1

        return total
