class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        knight_moves = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]
        
        def is_on_board(row, col):
            return 0 <= row < n and 0 <= col < n
        
        memo = {}
        def dp(level, row, col):
            if level == 0:
                return (1, 0) if is_on_board(row, col) else (0, 1)
            
            if not is_on_board(row, col):
                return (0, 8 ** level)
            
            if not (row, col, level) in memo:
                memo[(row, col, level)] = [0, 0]
                for r, c in knight_moves:
                    on_board, off_board = dp(level - 1, row + r, col + c)
                    memo[(row, col, level)][0] += on_board
                    memo[(row, col, level)][1] += off_board

            return memo[(row, col, level)]
        
        on_board, off_board = dp(k, row, column)
        return on_board / (on_board + off_board)
        
        