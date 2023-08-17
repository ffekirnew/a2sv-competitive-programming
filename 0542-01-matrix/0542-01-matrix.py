class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # define helper variables and functions
        ROWS, COLS = len(mat), len(mat[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        answer = [ [inf for c in range(COLS)] for r in range(ROWS) ]
        queue = deque([(r, c) for r in range(ROWS) for c in range(COLS) if mat[r][c] == 0])
        
        level = 0
        visited = set()
        while queue:
            next_level = []
            
            for row, col in queue:
                answer[row][col] = min(answer[row][col], level)
                
                visited.add((row, col))
                
                for r, c in DIRS:
                    nx_row, nx_col = row + r, col + c
                    
                    if in_bound(nx_row, nx_col) and (nx_row, nx_col) not in visited:
                        next_level.append((nx_row, nx_col))
                
            queue = next_level
            level += 1
        
        return answer
        
        
        
