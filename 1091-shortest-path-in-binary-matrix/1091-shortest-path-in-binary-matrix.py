class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        IN_BOUND = lambda row, col: 0 <= row < ROWS and 0 <= col < COLS
        
        DIRS = [ [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1] ]
        
        def bfs():
            if grid[0][0] == 1:
                return -1
            
            fringe = [(0, 0, [(0, 0)])]
            visited = set((0, 0))
            
            while fringe:
                next_level = []
                
                for row, col, curr_path in fringe:
                    if (row, col) == (ROWS - 1, COLS - 1):
                        return len(curr_path)
                    
                    for r, c in DIRS:
                        nx_row, nx_col = row + r, col + c
                        
                        if IN_BOUND(nx_row, nx_col) and (nx_row, nx_col) not in visited and grid[nx_row][nx_col] == 0:
                            visited.add((nx_row, nx_col))
                            fringe.append((nx_row, nx_col, curr_path + [(nx_row, nx_col)]))
                
                fringe = next_level
            
            return -1
        
        return bfs()
        