class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # We need to travel top to bottom
        # We need to find minimum distance
        # So it seems we need to try all paths
        # For every index there are four choices in the form of four directions.
        # So, we also need to store what are elements we already visted.
        # Lets say we are 0,0 and with empty set
        # We check weather row and columns are out of the limits if yes return maximum value
        # Then we see are at the last index if true return the value we got so far
        # we add the rows and columns to the set
        # we loop over to the all the four directions by adding abs to the value and passing it as param
        # we take the minimum value among them
        ROWS,COLS = len(heights),len(heights[0])

        minHeap = [[0,0,0]] #[diff,row,col]
        visit = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while minHeap:
            diff,r,c = heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            visit.add((r,c))

            if (r,c) == (ROWS-1,COLS-1):
                return diff
            
            for dr,dc in directions:
                newR,newC = r+dr,c+dc
                if(newR < 0 or newC < 0 or newR >= ROWS or newC >= COLS) or (newR,newC) in visit:
                    continue
                newDiff = max(diff,abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap,[newDiff,newR,newC])
        return 0
        
            