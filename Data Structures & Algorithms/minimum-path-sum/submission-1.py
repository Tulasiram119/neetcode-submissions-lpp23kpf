class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = set()
        rows,cols = len(grid),len(grid[0])
        heap = [[grid[0][0],0,0]]
        dirs = [[0,1],[1,0]]
        while heap:
            s,r,c = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if (r,c) == (rows-1,cols-1):
                return s
            for dr,dc in dirs:
                newr = r+dr
                newc = c+dc
                if newr >= rows or newc >= cols or newr < 0 or newc < 0 or (newr,newc) in visited:
                    continue
                heapq.heappush(heap,[s+grid[newr][newc],newr,newc])
        return -1
