class Solution:
    @staticmethod
    def out_of_order(board):
        out_of_order_pairs = 0
        for i in range(6):
            for j in range(i + 1, 6):
                if board[i] and board[j] and board[j] < board[i]:
                    out_of_order_pairs += 1
        return out_of_order_pairs
    
    @staticmethod
    def successor_states(board):
        states = []
        
        z_idx = [i for i in range(6) if board[i] == 0][0]
        
        if z_idx < len(board) - 1 and z_idx != 2:
            new_board = board.copy()
            new_board[z_idx], new_board[z_idx + 1] = new_board[z_idx + 1], new_board[z_idx]
            states.append(new_board)
        
        if z_idx != 3 and z_idx != 0:
            new_board = board.copy()
            new_board[z_idx], new_board[z_idx - 1] = new_board[z_idx - 1], new_board[z_idx]
            states.append(new_board)
        
        if  z_idx < 3:
            new_board = board.copy()
            new_board[z_idx], new_board[z_idx + 3] = new_board[z_idx + 3], new_board[z_idx]
            states.append(new_board)
        if z_idx > 2:
            new_board = board.copy()
            new_board[z_idx], new_board[z_idx - 3] = new_board[z_idx - 3], new_board[z_idx]
            states.append(new_board)
        
        return states

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # convert the board to a one dimensional board
        board = [board[r][c] for r in range(2) for c in range(3)]
        
        # check if the out of order numbers is an odd number, then there is no way to fix it
        if self.out_of_order(board) % 2:
            return -1
        
        # if it is solvable, do bfs
        
        queue = deque([[board, 0, []]])
        visited = set(tuple(board))
        while queue:
            state, moves, path = queue.popleft()
            
            if state == [1, 2, 3, 4, 5, 0]:
                return moves
            
            for successor in self.successor_states(state):
                if tuple(successor) not in visited:
                    visited.add(tuple(successor))
                    queue.append((successor, moves + 1, path + [successor]))            
        
        
        return 0
        