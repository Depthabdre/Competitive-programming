# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        graphBuild = defaultdict(list)
        arrayCount = [0]*len(graph)
        queue = deque()
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                graphBuild[graph[i][j]].append(i)
                arrayCount[i] += 1
        for i in range(len(arrayCount)):
            if arrayCount[i] == 0:
                queue.append(i)
        answer = []
        while queue:
            ele = queue.popleft()
            answer.append(ele)
            for u in graphBuild[ele]:
                arrayCount[u] -= 1
                if arrayCount[u] == 0:
                    queue.append(u)
        answer.sort()
        return answer