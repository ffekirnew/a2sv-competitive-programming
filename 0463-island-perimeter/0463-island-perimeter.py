class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dirs = [ [1, 0], [0, 1], [-1, 0], [0, -1] ]
        
        visited = [ [False for col in range(cols)] for row in range(rows) ]
        in_bound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        
        def dfs(row: int, col: int):
            visited[row][col] = True
            answer = 0
            
            for next_row, next_col in dirs:
                next_cell_row = row + next_row
                next_cell_col = col + next_col
                
                if in_bound(next_cell_row, next_cell_col):
                    answer += (grid[next_cell_row][next_cell_col] + 1) % 2
                    
                    if (not visited[next_cell_row][next_cell_col]) and (grid[next_cell_row][next_cell_col]):
                        answer += dfs(next_cell_row, next_cell_col)
                        
                else:
                    answer += 1
            
            return answer
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
                
            
            
            
        