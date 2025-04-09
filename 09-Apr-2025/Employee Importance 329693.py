# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        ans = 0

        for employe in employees:
            value = employe.importance
            neighbor = employe.subordinates
            lists = [value]
            some = neighbor
            lists.append(some)
            graph[employe.id].append(lists)

        def recursive(item):
            nonlocal ans
            lists = graph[item][0]
            if not lists[1]:
                ans += lists[0]
                return
            
            for it in lists[1]:
                recursive(it)
            ans += lists[0]
            return ans
        recursive(id)
        return ans
        