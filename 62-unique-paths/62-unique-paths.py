class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for col in range(n + 1)] for row in range(m + 1)]
        paths[-2][-2] = 1
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                paths[row][col] += paths[row][col] + paths[row][col + 1] + paths[row + 1][col]
        
        return paths[0][0] // 2
                    
                
        