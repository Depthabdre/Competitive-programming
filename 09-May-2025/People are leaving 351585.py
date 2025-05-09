# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, x):
        while x != self.parent[x]:     
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    


n, q = map(int, input().split())
uf = UnionFind(n)

for _ in range(q):
    typ, xs = input().split()
    x = int(xs)
    if typ == "?":
        print(uf.find(x))
    else:         
        if x == n:
            uf.parent[x] = -1
        else:
            uf.parent[x] = uf.find(x + 1)
