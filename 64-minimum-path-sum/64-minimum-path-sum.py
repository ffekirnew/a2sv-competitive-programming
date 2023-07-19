class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def in_bound(row: int, col: int):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dp(row, col):
            if not in_bound(row, col):
                return inf
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]
            
            if not (row, col) in memo:
                memo[(row, col)] = min(dp(row + 1, col), dp(row, col + 1)) + grid[row][col]
            
            return memo[(row, col)]
        
        return dp(0, 0)