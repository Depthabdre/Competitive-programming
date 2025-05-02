# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        result = []
        heap = []
        time = 0
        i = 0
        
        while i < len(tasks) or heap:
            if not heap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]
            while i < len(tasks) and indexed_tasks[i][0] <= time:
                et, pt, idx = indexed_tasks[i]
                heapq.heappush(heap, (pt, idx))
                i += 1
            if heap:
                pt, idx = heapq.heappop(heap)
                time += pt
                result.append(idx)
        
        return result
