class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[-1][-1] = 1 - obstacleGrid[-1][-1]
        
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if row == ROWS - 1 and col == COLS - 1:
                    continue

                if obstacleGrid[row][col]:
                    obstacleGrid[row][col] = 0
                    
                else:
                    if row + 1 < ROWS:
                        obstacleGrid[row][col] += obstacleGrid[row + 1][col]
                    if col + 1 < COLS:
                        obstacleGrid[row][col] += obstacleGrid[row][col + 1]
        
        return obstacleGrid[0][0]
            
        