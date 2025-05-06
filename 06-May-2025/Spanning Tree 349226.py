# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

import heapq

class unionFind:
    def __init__(self):
        self.parent = { }
        self.size = { }
    def find(self, x):
        while x != self.parent.setdefault(x, x):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, x, y):
        if x == y:
            return True
        py = self.find(x)
        px = self.find(y)
        if py != px:
            if self.size.get(px, 1) >= self.size.get(py, 1):
                self.parent[py] = px
                self.size[px] = self.size.get(px, 1) + self.size.get(py, 1)
            else:
                self.parent[px] = py
                self.size[py] = self.size.get(py, 1) + self.size.get(px, 1)
            return True
        else:
            return False
        
vertices , edges = map(int,input().split())
nums = []
uni = unionFind()
for i in range(edges):
    k , l , m = map(int,input().split())
    heapq.heappush(nums , (m , (k,l)))
total_sum = 0

while nums:
    k , ( l , m) = heapq.heappop(nums)
    if uni.union(l,m):
        total_sum += k

print(total_sum)
    


