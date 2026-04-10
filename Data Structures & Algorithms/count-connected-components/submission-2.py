class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set()
        def dfs(node):
            visit.add(node)
            for child in graph[node]:
                if child not in visit:
                    dfs(child)
        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                visit.add(i)
                dfs(i)
        return count