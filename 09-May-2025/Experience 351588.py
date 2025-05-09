# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

import sys

input = sys.stdin.readline

class DSUWithTags:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size   = [1]*(n+1)
       
        self.tag     = [0]*(n+1)
        
        self.delta   = [0]*(n+1)

    def find(self, x):
        """ Path-compress, and accumulate deltas on the way up. """
        if self.parent[x] != x:
            p = self.parent[x]
            root = self.find(p)
           
            self.delta[x] += self.delta[p]
            self.parent[x] = root
        return self.parent[x]

    def join(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
       
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
       
        self.delta[ry]  = self.tag[ry] - self.tag[rx]
        self.parent[ry] = rx
        self.size[rx]  += self.size[ry]

    def add(self, x, v):
        rx = self.find(x)
       
        self.tag[rx] += v

    def get(self, x):
        rx = self.find(x)
       
        return self.tag[rx] + self.delta[x]


n, m = map(int, input().split())
dsu = DSUWithTags(n)

for _ in range(m):
    qry = input().split()
    if qry[0] == "join":
        _, X, Y = qry
        dsu.join(int(X), int(Y))
    elif qry[0] == "add":
        _, X, V = qry
        dsu.add(int(X), int(V))
    else:  
        _, X = qry
        print(dsu.get(int(X)))
