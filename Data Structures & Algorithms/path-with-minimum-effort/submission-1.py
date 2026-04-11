import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # This table stores the minimum effort found to reach each cell
        # Initialize with infinity
        min_efforts = [[float('inf')] * cols for _ in range(rows)]
        min_efforts[0][0] = 0
        
        # Priority Queue: (current_max_effort, row, col)
        # We use a heap so we always process the path with the LOWEST effort first
        pq = [(0, 0, 0)]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            effort, r, c = heapq.heappop(pq)
            
            # If we reached the target, return immediately
            if r == rows - 1 and c == cols - 1:
                return effort
            
            # Optimization: If we found a better path to this cell already, skip it
            if effort > min_efforts[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    # The effort to get to the neighbor is the max of 
                    # our current effort and the jump to that neighbor
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    
                    # Only add to heap if this is better than any path found before
                    if new_effort < min_efforts[nr][nc]:
                        min_efforts[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
        
        return 0