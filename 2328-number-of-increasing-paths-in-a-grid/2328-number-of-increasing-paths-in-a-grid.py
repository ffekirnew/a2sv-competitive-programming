class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        visited = set()
        dp = [[1 for _ in range(COLS)] for _ in range(ROWS)]
        
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def dfs(row, col):
            if (row, col) in visited:
                return
            
            visited.add((row, col,))
            for r, c in DIRS:
                new_row = row + r
                new_col = col + c
                
                if not in_bound(new_row, new_col):
                    continue
                
                if grid[new_row][new_col] <= grid[row][col]:
                    continue
                
                dp[new_row][new_col] += dp[row][col]
                
        arr = sorted([ (grid[r][c], r, c) for r in range(ROWS) for c in range(COLS) ])
        
        sum_ = 0
        for _, r, c in arr:
            dfs(r, c)
            sum_ += dp[r][c]        
        
        return sum_ % (10 ** 9 + 7)
        
        
        
            
        