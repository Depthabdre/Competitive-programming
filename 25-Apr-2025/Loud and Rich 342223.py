# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)

        for richer , poorer in richer:
            graph[poorer].append(richer)
        answer = []
        small = 0
        memorization = {}
        def dfs(key):
            nonlocal small
            if key in memorization:
                if quiet[memorization[key]] <= quiet[small]:
                    small = memorization[key]
                return

            if len(graph[key]) == 0:
                if quiet[key] <= quiet[small]:
                    small = key
                return 
            if quiet[key] <= quiet[small]:
                small = key
            for richer in graph[key]:
                dfs(richer)

        for i in range(len(quiet)):
            small = i
            dfs(i)
            answer.append(small)
            memorization[i] = small
        return answer
        