from math import inf


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        
        def top_down(row, col):
            if not row < ROWS:
                return 0
             
            if not 0 <= col < COLS:
                return inf
            
            if (row, col) not in dp:
                dp[(row, col)] = min(top_down(row + 1, col), top_down(row + 1, col - 1), top_down(row + 1, col + 1)) + matrix[row][col]
            
            return dp[(row, col)]
        
        return min(top_down(0, col) for col in range(COLS))
        