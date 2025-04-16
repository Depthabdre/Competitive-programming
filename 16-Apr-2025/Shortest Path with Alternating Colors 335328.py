# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        bluegraph = defaultdict(list)
        redgraph = defaultdict(list)
        prev = -1 
        queue = deque()
        visited = set()

        for u , v in redEdges:
            redgraph[u].append(v)
            if u == 0:
                queue.append((v,'blue'))
                visited.add((0,'red'))
                visited.add((v,'blue'))
        for u , v in blueEdges:
            bluegraph[u].append(v)
            if u == 0:
                visited.add((0,'blue'))
                queue.append((v,'red'))
                visited.add((v,'red'))
        answer = [-1]*n
        answer[0] = 0
        level = 1
        
        while queue:
            print(queue)
            
            for i in range(len(queue)):
                node , color = queue.popleft()
                print(node,color,level)
                
                if answer[node] == -1:
                    answer[node] = level
                if color == 'red':
                    for nodes in redgraph[node]:
                        if (nodes , 'blue') not in visited:
                            queue.append((nodes,'blue'))
                            visited.add((nodes,'blue'))
                elif color == 'blue':
                    
                    for nodes in bluegraph[node]:
                        if (nodes , 'red') not in visited:
                            queue.append((nodes,'red'))
                            visited.add((nodes,'red'))
            level += 1
        return answer




        
        