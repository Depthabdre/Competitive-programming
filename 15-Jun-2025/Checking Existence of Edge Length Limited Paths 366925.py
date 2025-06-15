# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
       
        indexed_queries = [[p, q, limit, i] for i, (p, q, limit) in enumerate(queries)]

        
        edgeList.sort(key=lambda x: x[2])

        
        indexed_queries.sort(key=lambda x: x[2])

       
        res = [False] * len(queries)

        
        dsu = DSU(n)

       
        edge_i = 0

       
        for p, q, limit, idx in indexed_queries:
            
            while edge_i < len(edgeList) and edgeList[edge_i][2] < limit:
                u, v, _ = edgeList[edge_i]
                dsu.union(u, v)
                edge_i += 1

            
            if dsu.find(p) == dsu.find(q):
                res[idx] = True

        return res
