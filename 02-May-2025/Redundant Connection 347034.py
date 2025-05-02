# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self , n):
        self.parent = {i:i for i in range(1,n+1)}
        self.size = [1]*(n+1)
    def find(self , index):
        while index != self.parent[index]:
            self.parent[index] = self.parent[self.parent[index]]
            index = self.parent[index]
        return index
    def union(self,index1,index2):
        parent1 = self.find(index1)
        parent2 = self.find(index2)
        if parent1 == parent2:
            return True
        if self.size[parent1] > self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]
        return False




class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uni = UnionFind(len(edges))
        for i , j in edges:
            if uni.union(i,j):
                return [i,j]
        


        