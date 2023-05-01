import sys
sys.setrecursionlimit(100_000)

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def dfs(row, col):
            islands[-1].add((row, col))
            for r, c in DIRS:
                nx_row, nx_col = row + r, col + c
                
                if in_bound(nx_row, nx_col) and (nx_row, nx_col) not in visited and grid[nx_row][nx_col] == 1:
                    visited.add((nx_row, nx_col))
                    dfs(nx_row, nx_col)
        
        islands = []
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    islands.append(set())
                    dfs(r, c)
        
        min_distance = [inf]
        
        def bfs(row, col):
            queue = deque([(row, col, -1)])
            
            while queue:
                row, col, path_length = queue.popleft()
                
                if (row, col) in islands[1]:
                    min_distance[0] = min(min_distance[0], path_length)
                    break
                
                for r, c in DIRS:
                    nx_row, nx_col = row + r, col + c
                    
                    if in_bound(nx_row, nx_col) and (nx_row, nx_col) not in visited and (nx_row, nx_col) not in islands[0]:
                        visited.add((nx_row, nx_col))
                        queue.append((nx_row, nx_col, path_length + 1))
        
        
        for row, col in islands[0]:
            visited = set((row, col))
            bfs(row, col)
            
        return min_distance[0]