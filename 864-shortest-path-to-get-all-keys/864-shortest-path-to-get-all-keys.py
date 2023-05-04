class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def successor_positions(row, col):
            positions = []
            for r, c in DIRS:
                nx_row, nx_col = row + r, col + c
                
                if not in_bound(nx_row, nx_col):
                    continue
                
                if grid[nx_row][nx_col] == '#':
                    continue
                    
                if 'A' <= grid[nx_row][nx_col] <= 'Z' and grid[nx_row][nx_col].lower() not in keys_found:
                    continue
                
                positions.append([nx_row, nx_col])
            
            return positions

        curr_position = [(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == '@'][0]
        keys_left = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                keys_left += 'A' <= grid[r][c] <= 'Z'
        
        queue = deque([ [curr_position[0], curr_position[1], [], []] ])
        visited = set([tuple([curr_position[0], curr_position[1]])])
        min_moves = inf

        while queue:
            r, c, path, keys_found = queue.popleft()

            if len(keys_found) == keys_left:
                return len(path)
            
            for row, col in successor_positions(r, c):
                if (row, col, tuple(keys_found)) not in visited:
                    if 'a' <= grid[row][col] <= 'z' and grid[row][col] not in keys_found:
                        new_keys = keys_found + [grid[row][col]]
                    else:
                        new_keys = keys_found.copy()
                    
                    visited.add((row, col, tuple(keys_found)))
                    queue.append([row, col, path + [(row, col)], new_keys])
        
        if min_moves == inf:
            return -1
        
        return min_moves
        