class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # Os and Xs
        Os, Xs = 0, 0
        
        for row in board:
            Xs += row.count("X")
            Os += row.count("O")
        
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
        
        winners = Counter(lines)
        
        if winners["XXX"] and winners["OOO"]:
            return False
        elif winners["XXX"] and Xs != Os + 1:
            return False
        elif winners["OOO"] and Os != Xs:
            return False
        else:
            return True
        