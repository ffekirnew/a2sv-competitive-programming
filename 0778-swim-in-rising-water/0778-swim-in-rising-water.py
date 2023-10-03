from math import inf
from heapq import heappop, heappush


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Set up Dijkstra
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def is_in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
    
        # Implement dijkstra
        heap = [(grid[0][0], grid[0][0], 0, 0)] # [(depth, row, col),...]
        visited = set([])
        while heap:
            _, depth, row, col = heappop(heap)
            visited.add((row, col))
            
            if (row, col) == (ROWS - 1, COLS - 1):
                return depth
            
            for r, c in dirs:
                nx_row, nx_col = row + r, col + c
                
                if is_in_bound(nx_row, nx_col) and (nx_row, nx_col) not in visited:
                    heappush(heap, (grid[nx_row][nx_col], max(depth, grid[nx_row][nx_col]), nx_row, nx_col ))
        
        return -inf
        
        
        