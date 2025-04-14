# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        tree = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

       
        def dfs(emp_id):
            if not tree[emp_id]: 
                return 0
            max_time = 0
            for sub in tree[emp_id]:
                max_time = max(max_time, dfs(sub))
            return informTime[emp_id] + max_time

        return dfs(headID)
