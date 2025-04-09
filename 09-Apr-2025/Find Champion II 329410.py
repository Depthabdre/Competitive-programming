# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n==1:
            return 0
        graph = defaultdict(list)
        val = set(range(0,n))

        for node1, node2 in edges:
            graph[node1].append(node2)
            if node1 in val:
                val.remove(node1)
            if node2 in val:
                val.remove(node2)
        if len(val) != 0:
            return -1

        potential_ans = defaultdict(set)

        def recursive(key,item):
            if item not in graph:
                if item in potential_ans:
                    del potential_ans[item]
                potential_ans[key].add(item)
                
                return
            for it in graph[item]:
                recursive(key,it)
                if it in potential_ans:
                    del potential_ans[it]
                potential_ans[key].add(it)
            del graph[item]
            return 
        while graph:
            key = next(iter(graph))
            recursive(key,key)
           
            

        if len(potential_ans) == 1:
            return next(iter(potential_ans))
        else:
            return -1
