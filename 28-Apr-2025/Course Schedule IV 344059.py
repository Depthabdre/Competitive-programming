# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        reach = [[False] * n for _ in range(n)]
        for i in range(n):
            reach[i][i] = True
        for u, v in prerequisites:
            reach[u][v] = True
        for k in range(n):
            for i in range(n):
                if reach[i][k]:
                    for j in range(n):
                        reach[i][j] |= reach[k][j]
        answer = []
        for u, v in queries:
            answer.append(reach[u][v])
        return answer
