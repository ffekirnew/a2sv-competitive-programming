class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        answer = 0
        
        for row_start in range(rows - 2):
            for col_start in range(cols - 2):
                row_sum = [0, 0, 0]
                col_sum = [0, 0, 0]
                diagonal_sum = [0, 0]
                occurence = {}
                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):
                        occurence[grid[r][c]] = occurence.get(grid[r][c], 0) + 1
                        row_sum[r - row_start] += grid[r][c]
                        col_sum[c - col_start] += grid[r][c]
                        if r - row_start == c - col_start:
                            diagonal_sum[0] += grid[r][c]
                        if (r - row_start) + (c - col_start) == 2:
                            diagonal_sum[1] += grid[r][c]
                            
                all_sum_equal = (row_sum[0] == row_sum[1] == row_sum[2] == col_sum[0] == col_sum[1] == col_sum[2] == diagonal_sum[0] == diagonal_sum[1])
                all_only_once = all(map(lambda x: x[1] == 1 and 0 < x[0] < 10, list(occurence.items())))
                occurence.clear()
                
                if all_sum_equal and all_only_once:
                    answer += 1
        
        return answer
        