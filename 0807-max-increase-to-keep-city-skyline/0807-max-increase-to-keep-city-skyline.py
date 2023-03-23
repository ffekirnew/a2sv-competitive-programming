class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [ max([ grid[row][col] for row in range(len(grid)) ]) for col in range(len(grid)) ]

        answer = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not (grid[row][col] == row_max[row] or grid[row][col] == col_max[col]):
                    answer += min(row_max[row], col_max[col]) - grid[row][col]
        
        return answer
                
        