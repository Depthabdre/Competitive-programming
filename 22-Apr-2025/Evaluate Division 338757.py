# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        given_answer = defaultdict(int)

        for i , (u , v ) in enumerate(equations):
            given_answer[(u,v)] = values[i]
            given_answer[(v,u)] = 1 / values[i] 
        
        for u , v in equations:
            graph[u].append(v)
            graph[v].append(u)

        def bfs (u , v , visited):
            # prev curr answer
            queue = deque([[u , 1]])
            visited.add(u)
            if u == v:
                if len(graph[u]) > 0:
                    return 1
                else:
                    return - 1
            while queue:
                for i in range(len(queue)):
                    prev , answer = queue.popleft()

                    for curr in graph[prev]:
                        if curr not in visited:
                            ans =  answer * given_answer[(prev,curr)] 
                            if curr == v:
                                return ans
                            queue.append([curr,ans])
                            visited.add(curr)
            return - 1

        answer = []
        for u , v in queries:
            visited = set()
            answer.append(bfs(u,v,visited))
        return answer
        

        