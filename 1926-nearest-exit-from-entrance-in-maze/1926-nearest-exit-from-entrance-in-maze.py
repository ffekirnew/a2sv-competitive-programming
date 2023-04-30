class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def is_border(row, col):
            return any( not in_bound(row + r, col + c) for r, c in DIRS )
        
        queue = deque([tuple([entrance[0], entrance[1], 0])])
        visited = set(tuple(entrance))
        
        while queue:
            curr_row, curr_col, path_length = queue.popleft()
            
            if is_border(curr_row, curr_col) and [curr_row, curr_col] != entrance:
                return path_length
            
            for r, c in DIRS:
                nx_row, nx_col = curr_row + r, curr_col + c
                
                if (nx_row, nx_col) not in visited and in_bound(nx_row, nx_col) and maze[nx_row][nx_col] != '+':
                    visited.add((nx_row, nx_col))
                    queue.append((nx_row, nx_col, path_length + 1))
        
        return -1
        