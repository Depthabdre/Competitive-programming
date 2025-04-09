# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        
        for i in range(len(isConnected[0])):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        
        selected = set()
        answer = 0

        def recursive(item):
            
            for it in graph[item]:
                if it in selected:
                    continue
                selected.add(it)
                recursive(it)
            del graph[item]
            return 
        while graph:
            key = next(iter(graph))
            selected.add(key)
            recursive(key)
            selected=set()
            answer += 1
        return answer
            

           
            

        
        