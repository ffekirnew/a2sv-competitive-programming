class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for col in range(n)] for row in range(m)]
        paths[-1][-1] = 1
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row + 1 < m:
                    paths[row][col] += paths[row + 1][col]
                if col + 1 < n:
                    paths[row][col] += paths[row][col + 1]
        
        return paths[0][0]
                    
                
        