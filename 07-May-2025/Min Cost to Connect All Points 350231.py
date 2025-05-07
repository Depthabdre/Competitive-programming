# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

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
          


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        for i in range(len(points)):
            for j in range(i + 1 , len(points)):
                distances.append([(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])) , (i,j)] )
        heapify(distances)
        uni = unionFind()
        answer = 0
        while distances:
    
            values , nodes = heappop(distances)
            
           
            pt1 = uni.find(nodes[0])
            pt2 = uni.find(nodes[1])
           
            if pt1 != pt2:
                answer += values
                uni.union(nodes[0] , nodes[1])
        return answer
        
        


        