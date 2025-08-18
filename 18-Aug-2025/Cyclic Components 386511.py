# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

# Abdre
import sys
from collections import defaultdict

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


def solve():
    n, m = map(int, sys.stdin.readline().split())
    ufds = uf(n)
    indegree = [0] * (n + 1)

   
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        indegree[u] += 1
        indegree[v] += 1
        ufds.union(u, v)

   
    comp = defaultdict(list)
    for v in range(1, n + 1):
        root = ufds.find(v)
        comp[root].append(v)

    
    ans = 0
    for vertices in comp.values():
        if len(vertices) >= 3 and all(indegree[v] == 2 for v in vertices):
            ans += 1

    print(ans)


if __name__ == "__main__":
    solve()
