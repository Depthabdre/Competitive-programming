# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times, n, k):
       
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        
        heap = [(0, k)]  
        shortest = dict()  

        while heap:
            time, node = heapq.heappop(heap)
            if node in shortest:
                continue 
            shortest[node] = time
            for neighbor, weight in graph[node]:
                if neighbor not in shortest:
                    heapq.heappush(heap, (time + weight, neighbor))

        
        if len(shortest) == n:
            return max(shortest.values())
        else:
            return -1
