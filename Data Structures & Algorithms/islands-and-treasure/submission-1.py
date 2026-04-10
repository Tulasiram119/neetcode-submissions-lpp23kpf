class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        def addRooms(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or grid[r][c] == -1:
                return 
            visit.add((r,c))
            q.append([r,c])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    q.append([i,j]) 
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRooms(r+1,c)
                addRooms(r-1,c)
                addRooms(r,c+1)
                addRooms(r,c-1)
            dist += 1