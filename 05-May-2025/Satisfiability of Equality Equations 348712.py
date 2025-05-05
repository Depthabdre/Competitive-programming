# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

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


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        uni = unionFind()
        for equa in equations:
            if equa[1] != '!':
                uni.union(equa[0] , equa[-1])
        
        for equa in equations:
            if equa[1] == '!':
                parent1 = uni.find(equa[0])
                parent2 = uni.find(equa[-1])
                if parent1 == parent2:
                    return False

        return True