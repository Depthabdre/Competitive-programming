# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class unionFind:
    def __init__(self, n):
        self.parent = {(i, j) : (i, j) for i in range(n + 1) for j in range(n + 1)}
        self.size = {(i, j) : 1 for i in range(n + 1) for j in range(n + 1)}
        self.n = n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]
    def corner(self, a, b):
        if (0 in a or self.n in a) and (0 in b or self.n in b):
            return True
        return False
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            if not self.corner(parentX, parentY):
                print(parentX, parentY)
                if 0 in parentX or self.n in parentX:
                    self.parent[parentY] = parentX
                    self.size[parentX] += self.size[parentY]
                elif 0 in parentY or self.n in parentY:
                    self.parent[parentX] = parentY
                    self.size[parentY] += self.size[parentX]
                elif self.size[parentX] > self.size[parentY]:
                    self.parent[parentY] = parentX
                    self.size[parentX] += self.size[parentY]
                else:
                    self.parent[parentX] = parentY
                    self.size[parentY] += self.size[parentX]
                return 0
            else:
                return 1
        return 1
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ans = 1
        uni = unionFind(len(grid))
        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch == "/":
                    ans += uni.union((i + 1, j), (i, j + 1))
                elif ch == "\\":
                    ans += uni.union((i, j), (i + 1, j + 1))
                    j += 1
        return ans
