# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class uf:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return self.par[node]
    
    def union(self, u, v):
        par_u = self.find(u)
        par_v = self.find(v)

        if par_u == par_v:
            return False
        if self.size[par_u] < self.size[par_v]:
            par_u, par_v = par_v, par_u
        
        self.par[par_v] = par_u
        self.size[par_u] += self.size[par_v]
        return True
    
    def checker(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse = True)
        total = 0
        aliceUnion = uf(n)
        bobUnion = uf(n)

        for typ , u , v in edges:
            if typ == 1:
                if aliceUnion.find(u) == aliceUnion.find(v):
                    total += 1
                else:
                    aliceUnion.union(u,v)
            elif typ == 2:
                if bobUnion.find(u) == bobUnion.find(v):
                    total += 1
                else:
                    bobUnion.union(u,v)
            else:
                if (aliceUnion.find(u) == aliceUnion.find(v)) and (bobUnion.find(u) == bobUnion.find(v)):
                    total += 1
                else:
                    aliceUnion.union(u,v)
                    bobUnion.union(u,v)
        pt = aliceUnion.find(1)
        pt2 = bobUnion.find(1)
        if aliceUnion.size[pt] == n and bobUnion.size[pt2] == n:
            return total
        else:
            return -1
                