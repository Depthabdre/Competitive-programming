# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

class unionFind:
    def __init__(self , n):
        self.parent = {i:i for i in range(n+1) }
        self.size = {i:1 for i in range(n+1) }
    def find(self, x):
        while x != self.parent.setdefault(x, x):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, x, y):
        py = self.find(x)
        px = self.find(y)
        if py != px:
            if self.size.get(px, 1) >= self.size.get(py, 1):
                self.parent[py] = px
                self.size[px] = self.size.get(px, 1) + self.size.get(py, 1)
            else:
                self.parent[px] = py
                self.size[py] = self.size.get(py, 1) + self.size.get(px, 1)
            

len_node , len_edges , len_operation = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(len_edges)]
operation = [input().split() for _ in range(len_operation)]
uni = unionFind(len_node)
answer = []
for i in range(1,len_operation+1):
    if operation[-i][0] == "ask":
        parentx = uni.find(int(operation[-i][1]))
        parenty = uni.find(int(operation[-i][2]))
        if parentx == parenty:
            answer.append("YES")
        else:
            answer.append("NO")
    else:
        uni.union(int(operation[-i][1]),int(operation[-i][2]))

for i in range(1,len(answer) + 1):
    print(answer[-i])
        