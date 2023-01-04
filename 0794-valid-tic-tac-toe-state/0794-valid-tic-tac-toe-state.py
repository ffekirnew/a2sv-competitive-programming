class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # Os and Xs
        Os, Xs = "".join(board).count("O"), "".join(board).count("X")
        
        if Os > Xs or Xs > Os + 1:
            return False

        # identify all lines
        lines = set(board)
        for col in range(3):
            line = ""
            for row in range(3):
                line += board[row][col]
            lines.add(line)

        lines.add(board[0][0] + board[1][1] + board[2][2])
        lines.add(board[2][0] + board[1][1] + board[0][2])
        
        if "XXX" in lines and "OOO" in lines:
            return False
        elif "XXX" in lines and Xs != Os + 1 or "OOO" in lines and Os != Xs:
            return False
        else:
            return True
        