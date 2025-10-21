# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

import heapq
from collections import defaultdict

def dijkstra_maxheap(graph, start_node, last):
    distances = {node: 0 for node in graph}  
    distances[start_node] = 1  

    heap = [(-1, start_node)]  

    while heap:
        current_prob_neg, current_node = heapq.heappop(heap)
        current_prob = -current_prob_neg

        for neighbor, weight in graph[current_node]:
            prob = current_prob * weight
            if prob > distances[neighbor]:
                distances[neighbor] = prob
                heapq.heappush(heap, (-prob, neighbor))

    return distances[last]

class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        graph = defaultdict(list)
        for i in range(n):
            graph[i] = []  

        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        return dijkstra_maxheap(graph, start_node, end_node)
