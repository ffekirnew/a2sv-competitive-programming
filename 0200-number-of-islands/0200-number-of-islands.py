class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dirs = [ [1, 0], [0, 1], [-1, 0], [0, -1] ]
        
        in_bound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        
        def dfs(row: int, col: int):
            grid[row][col] = "0"
            
            for next_row, next_col in dirs:
                next_cell_row = row + next_row
                next_cell_col = col + next_col
                
                if in_bound(next_cell_row, next_cell_col) and grid[next_cell_row][next_cell_col] == "1":
                    dfs(next_cell_row, next_cell_col)
        
        answer = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    answer += 1
        
        return answer
                
            
            
            
        