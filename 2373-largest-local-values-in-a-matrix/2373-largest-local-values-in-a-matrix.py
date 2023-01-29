class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        result = []
        
        for row in range(0, rows - 2):
            result.append([])
            for col in range(0, cols - 2):
                r, c = row, col
                maximum = grid[r][c]
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        maximum = max(maximum, grid[r][c])
                result[-1].append(maximum)
            
        return result
                
                    
        