class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        IN_BOUND = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS
        
        def bfs(rotten_list):
            if not rotten_list:
                return 0

            visited = set()
            minutes = -1
            
            while rotten_list:
                minutes += 1
                
                next_level = []
                
                for row, col in rotten_list:
                    grid[row][col] = 2
                    for r, c in DIRS:
                        nx_row, nx_col = row + r, col + c
                        
                        if (nx_row, nx_col) not in visited and IN_BOUND(nx_row, nx_col) and grid[nx_row][nx_col] == 1:
                            visited.add((nx_row, nx_col))
                            next_level.append((nx_row, nx_col,))
                
                rotten_list = next_level
                
            return minutes
        
        rotten_list = [(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 2]
                    
        answer = bfs(rotten_list)
        
        if all(grid[r][c] != 1 for r in range(ROWS) for c in range(COLS)):
            return answer

        return -1
                    
                    
                    
                
        