class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
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
                dfs(i)
        return count