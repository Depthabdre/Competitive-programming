# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_graph = defaultdict(list)
        item_indegree = [0] * n
        group_graph = defaultdict(list)
        group_indegree = [0] * m
        group_items = defaultdict(list)

        for i in range(n):
            group_items[group[i]].append(i)

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1
                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        def topo_sort(nodes, graph, indegree):
            res = []
            queue = deque([node for node in nodes if indegree[node] == 0])
            while queue:
                node = queue.popleft()
                res.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            return res if len(res) == len(nodes) else []

        item_order = topo_sort(list(range(n)), item_graph, item_indegree)
        group_order = topo_sort(list(range(m)), group_graph, group_indegree)

        if not item_order or not group_order:
            return []

        ordered_items_in_group = defaultdict(list)
        for item in item_order:
            ordered_items_in_group[group[item]].append(item)

        res = []
        for grp in group_order:
            res.extend(ordered_items_in_group[grp])
        return res
