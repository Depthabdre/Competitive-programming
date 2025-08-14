# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
      
        graph = [[] for _ in range(n)]      
        incoming = [0 for _ in range(n)]   
        for parent, child in edges:
            graph[parent].append(child)
            incoming[child] += 1           

        
        queue = deque([i for i in range(n) if incoming[i] == 0])

        
        answer = [set() for _ in range(n)]  

        
        while queue:
            parent = queue.popleft()
            for child in graph[parent]:
                
                answer[child].add(parent)
               
                answer[child].update(answer[parent])
                
                incoming[child] -= 1
               
                if incoming[child] == 0:
                    queue.append(child)

        
        return [sorted(list(ancestors)) for ancestors in answer]
