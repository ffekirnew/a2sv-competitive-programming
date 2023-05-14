class Solution:
            
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        def is_move_possible(x: int, y: int, number: str) -> bool:
            if board[x][y] != '.':
                return False

            for loc in range(9):
                if board[loc][y] == number or board[x][loc] == number:
                    return False

            curr_square = set()
            row_start, col_start = (x // 3) * 3, (y // 3) * 3
            for row in range(row_start, row_start + 3):
                for col in range(col_start, col_start + 3):
                    if board[row][col] != '.' and board[row][col] in curr_square:
                        return False
                    curr_square.add(board[row][col])

            return True
        
        def solve():
            for x in range(9):
                for y in range(9):
                    if board[x][y] == '.':
                        for number in numbers:
                            if is_move_possible(x, y, number):
                                board[x][y] = number
                                if solve():
                                    return True
                                board[x][y] = '.'
                        return False
            return True
        
        solve()