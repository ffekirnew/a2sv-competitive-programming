class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        DIRS = [ [0, 1], [1, 0] ]
        
        paths = [[0 for col in range(COLS)] for row in range(ROWS)]
        paths[-1][-1] = 1
        
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if obstacleGrid[row][col]:
                    paths[row][col] = 0
                
                else:
                    if row + 1 < ROWS:
                        paths[row][col] += paths[row + 1][col]
                    if col + 1 < COLS:
                        paths[row][col] += paths[row][col + 1]
        
        return paths[0][0]
            
        