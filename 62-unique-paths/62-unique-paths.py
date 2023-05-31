class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[inf for col in range(n)] for row in range(m)]
        paths[-1][-1] = 1
        
        def get_paths(row, col):
            return 0 if row >= m or col >= n else paths[row][col]
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if paths[row][col] != inf:
                    continue
                paths[row][col] = get_paths(row + 1, col) + get_paths(row, col + 1)
        
        return paths[0][0]
                    
                
        