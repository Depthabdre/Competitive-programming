# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

       
        best = [[] for _ in range(n + 1)]

        heap = [(0, 1)]

        while heap:
            curr_time, node = heapq.heappop(heap)

           
            if len(best[node]) == 2:
                continue

         
            if not best[node] or best[node][-1] != curr_time:
                best[node].append(curr_time)
            else:
                continue  

           
            if node == n and len(best[node]) == 2:
                return best[node][1]

          
            if (curr_time // change) % 2 == 1:  
                curr_time = (curr_time // change + 1) * change  

           
            for nei in graph[node]:
                new_time = curr_time + time
                if len(best[nei]) < 2:
                    heapq.heappush(heap, (new_time, nei))
