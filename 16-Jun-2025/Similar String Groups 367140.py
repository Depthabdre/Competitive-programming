# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
       
        n = len(strs)
        parent = list(range(n))

       
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

       
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py  

       
        def areSimilar(s1, s2):
            diff = []
            for a, b in zip(s1, s2):
                if a != b:
                    diff.append((a, b))
                    if len(diff) > 2:
                        return False
            if len(diff) == 0:
                return True
            if len(diff) == 2 and diff[0] == diff[1][::-1]:
                return True
            return False

      
        for i in range(n):
            for j in range(i + 1, n):
                if areSimilar(strs[i], strs[j]):
                    union(i, j)

        
        groups = set()
        for i in range(n):
            groups.add(find(i))
        return len(groups)
