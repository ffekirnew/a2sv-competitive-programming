class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs and memoization
        memo = {}
        
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def in_bound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            
            max_of_childs = 0
            for r, c in DIRS:
                new_row = row + r
                new_col = col + c
                
                if not in_bound(new_row, new_col):
                    continue
                
                if matrix[new_row][new_col] <= matrix[row][col]:
                    continue
                    
                max_of_childs = max( max_of_childs, dfs(new_row, new_col) )
            
            memo[(row, col)] = max_of_childs + 1
            return  memo[(row, col)]
        
        max_length = 1
        
        for i in range(ROWS):
            for j in range(COLS):
                max_length = max( max_length, dfs(i, j) )
        
        return max_length
        
        
            
        