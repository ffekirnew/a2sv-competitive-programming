from math import inf
from heapq import heappop, heappush


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Set up Dijkstra
        ROWS, COLS = len(grid), len(grid[0])
        distances = [[[inf for _ in range(k + 1)] for __ in range(COLS)] for ___ in range(ROWS)]

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def is_in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        # Implement dijkstra
        heap = [(0, 0, 0, k)] # [(weight, row, col, eliminations_left),...]
        visited = set([])

        while heap:
            weight, row, col, eliminations_left = heappop(heap)
            visited.add((row, col, eliminations_left))
            
            if (row, col) == (ROWS - 1, COLS - 1):
                return weight
            
            for r, c in dirs:
                nx_row, nx_col = row + r, col + c
                
                if is_in_bound(nx_row, nx_col) and (nx_row, nx_col, eliminations_left) not in visited and distances[nx_row][nx_col][eliminations_left] > weight:
                    distances[nx_row][nx_col][eliminations_left] = weight
                    if eliminations_left > 0 or grid[nx_row][nx_col] == 0:
                        heappush(heap, ( weight + 1, nx_row, nx_col, eliminations_left - grid[nx_row][nx_col] ))
        
        return -1