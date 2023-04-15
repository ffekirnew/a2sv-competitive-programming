class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dirs = [ [1, 0], [0, 1], [-1, 0], [0, -1] ]
        
        in_bound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        
        def dfs(row: int, col: int):
            components = 1
            grid[row][col] = 0
            
            for next_row, next_col in dirs:
                next_cell_row = row + next_row
                next_cell_col = col + next_col
                
                if in_bound(next_cell_row, next_cell_col) and grid[next_cell_row][next_cell_col]:
                    components += dfs(next_cell_row, next_cell_col)
            
            return components
        
        max_island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    max_island = max( dfs(i, j), max_island )
        
        return max_island
        