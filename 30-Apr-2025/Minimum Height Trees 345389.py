# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        remaining_nodes = n
        
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves
