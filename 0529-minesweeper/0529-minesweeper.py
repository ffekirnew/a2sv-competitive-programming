class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            
            return board
        
        rows = len(board)
        cols = len(board[0])
        
        def in_bound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        
        dirs = [ [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1] ]
        def count_mines_around(row, col):
            answer = 0
            non_mines = []
            
            for r, c in dirs:
                if in_bound(row + r, col + c):
                    if board[row + r][col + c] == 'M':
                        answer += 1
                    else:
                        non_mines.append((row + r, col + c,))
            
            return answer, non_mines
        
        
        fringe = [(click[0], click[1],)]
        visited = set()
        
        while fringe:
            row, col = fringe.pop()
            adj_mines, adj_empties = count_mines_around(row, col)
            
            if adj_mines:
                board[row][col] = str(adj_mines)
            else:
                board[row][col] = 'B'
                for next_cell in adj_empties:
                    if next_cell not in visited:
                        visited.add(next_cell)
                        fringe.append(next_cell)
        
        return board
            
            
            
            
                
                    