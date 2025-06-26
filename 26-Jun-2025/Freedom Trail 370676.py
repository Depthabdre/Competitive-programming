# Problem: Freedom Trail - https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        graph = defaultdict(list)

        for i, ch in enumerate(ring):
            graph[ch].append(i)

        @lru_cache(None)
        def dfs(pos, ki):
            if ki == len(key):
                return 0

            res = float('inf')
            for i in graph[key[ki]]:
                dist = abs(i - pos)
                step = min(dist, n - dist)
                res = min(res, step + 1 + dfs(i, ki + 1))
            return res

        return dfs(0, 0)
