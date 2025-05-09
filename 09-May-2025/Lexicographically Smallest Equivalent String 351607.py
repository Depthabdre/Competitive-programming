# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class unionFind:
    def __init__(self):
        self.parent = { }
    def find(self, x):
        while x != self.parent.setdefault(x, x):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, x, y):
        py = self.find(x)
        px = self.find(y)
        if py != px:
            if px <= py:
                self.parent[py] = px
               
            else:
                self.parent[px] = py
                
           

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = unionFind()
        for i in range(len(s1)):
            uf.union(s1[i] , s2[i])
        answer = []

        for char in baseStr:
            answer.append(uf.find(char))
    
        return "".join(answer)

        