# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict

num_nodes, num_edges = map(int, input().split())
graph = defaultdict(list)

for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  


degrees = [0] * num_nodes
for node in graph:
    degrees[node-1] = len(graph[node])


for node in range(num_nodes):
    if degrees[node] == num_nodes - 1:
        if degrees.count(1) == num_nodes - 1:
            print("star topology")
            break
else:
   
    if degrees.count(1) == 2 and degrees.count(2) == num_nodes - 2:
        print("bus topology")
    
    elif degrees.count(2) == num_nodes:
        print("ring topology")
    else:
        print("unknown topology")
