# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid):
       
        m, n = len(targetGrid), len(targetGrid[0])
        bounds = dict()
        colors = set()
        
       
        for r in range(m):
            for c in range(n):
                color = targetGrid[r][c]
                colors.add(color)
                if color not in bounds:
                    bounds[color] = [r, r, c, c]
                else:
                    bounds[color][0] = min(bounds[color][0], r)
                    bounds[color][1] = max(bounds[color][1], r)
                    bounds[color][2] = min(bounds[color][2], c)
                    bounds[color][3] = max(bounds[color][3], c)
        
       
        graph = defaultdict(set)
        indegree = defaultdict(int)
        
        for color in colors:
            top, bottom, left, right = bounds[color]
            for r in range(top, bottom+1):
                for c in range(left, right+1):
                    other = targetGrid[r][c]
                    if other != color:
                        if other not in graph[color]:
                            graph[color].add(other)
                            indegree[other] += 1
        
       
        queue = deque()
        for color in colors:
            if indegree[color] == 0:
                queue.append(color)
        
        printed = 0
        while queue:
            curr = queue.popleft()
            printed += 1
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return printed == len(colors)
