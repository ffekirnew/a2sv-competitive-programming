class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols, rows = 9, 9
        
        # search row wise
        for row in range(rows):
            curr_row = set()
            for col in range(cols):
                if board[row][col] != '.' and board[row][col] in curr_row:
                    return False
                curr_row.add(board[row][col])
            curr_row.clear()

        # search column wise
        for col in range(cols):
            curr_col = set()
            for row in range(cols):
                if board[row][col] != '.' and board[row][col] in curr_col:
                    return False
                curr_col.add(board[row][col])
            curr_col.clear()

        # search square wise
        for r in range(0, rows, 3):
            for c in range(0, rows, 3):
                curr_square = set()
                for row in range(r, r + 3):
                    for col in range(c, c + 3):
                        if board[row][col] != '.' and board[row][col] in curr_square:
                            return False
                        curr_square.add(board[row][col])
                curr_square.clear()
        
        return True
                        
                
                