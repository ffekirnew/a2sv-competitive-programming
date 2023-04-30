import sys
sys.setrecursionlimit(40_000)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # find all regions' coordinates
        
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(board)
        COLS = len(board[0])
        
        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def neighbours_in_bound(row, col):
            return all( in_bound(row + r, col + c) for r, c in DIRS )
        
        all_regions = []
        visited = set()
        def dfs(row, col):
            all_regions[-1].append((row, col,))
            visited.add(tuple([row, col]))
            
            for r, c in DIRS:
                new_row, new_col = row + r, col + c
                
                if tuple([new_row, new_col]) not in visited and in_bound(new_row, new_col) and board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if tuple([r, c]) not in visited and board[r][c] == 'O':
                    all_regions.append([])
                    dfs(r, c)
        
        for region in all_regions:
            if any(not neighbours_in_bound(row, col) for row, col in region):
                continue
            
            for row, col in region:
                board[row][col] = 'X'
                
                
            
        