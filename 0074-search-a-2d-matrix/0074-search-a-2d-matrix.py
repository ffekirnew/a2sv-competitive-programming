class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row and cols for simplicity
        rows = len(matrix)
        cols = len(matrix[0])

        start_row = 0
        end_row = rows - 1
        
        while start_row <= end_row:
            middle_row = (start_row + end_row) // 2
            
            if matrix[middle_row][0] <= target <= matrix[middle_row][cols - 1]:
                start_col = 0
                end_col = cols - 1
                
                while start_col <= end_col:
                    middle_col = (start_col + end_col) // 2
                    
                    if matrix[middle_row][middle_col] == target:
                        return True
                    elif matrix[middle_row][middle_col] > target:
                        end_col = middle_col - 1
                    else:
                        start_col = middle_col + 1
                        
                return False

            elif target > matrix[middle_row][cols - 1]:
                start_row = middle_row + 1
            else:
                end_row = middle_row - 1
        
        return False
            
        