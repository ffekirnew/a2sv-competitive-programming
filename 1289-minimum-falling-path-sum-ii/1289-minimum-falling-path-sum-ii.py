class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        for row in range(ROWS - 2, -1, -1):
            for row_col in range(COLS):
                min_below = inf
                for col in range(COLS):
                    if row_col == col:
                        continue
                    min_below = min(min_below, grid[row + 1][col])
                grid[row][row_col] = grid[row][row_col] + min_below
        
        return min(grid[0])