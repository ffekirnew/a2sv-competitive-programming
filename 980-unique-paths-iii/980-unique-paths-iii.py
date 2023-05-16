class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        num_empty_cells = sum(row.count(0) for row in grid)
        
        starting_cell = [(r, c,) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 1][0]
        ending_cell = [(r, c,) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 2][0]
        
        answer = [0]
        def dfs(row, col, curr_empty_cells, curr_path):
            if grid[row][col] == 0:
                curr_empty_cells += 1

            if (row, col) == ending_cell:
                if curr_empty_cells == num_empty_cells:
                    answer[0] += 1
                return
            
            for r, c in DIRS:
                nx_row, nx_col = row + r, col + c
                
                if not in_bound(nx_row, nx_col):
                    continue
                
                if grid[nx_row][nx_col] == -1:
                    continue

                if (nx_row, nx_col) in curr_path:
                    continue

                dfs(nx_row, nx_col, curr_empty_cells, curr_path + [(nx_row, nx_col)] )
            
            return
        

        dfs(starting_cell[0], starting_cell[1], 0, [(starting_cell[0], starting_cell[1])])
        return answer[0]
            
        