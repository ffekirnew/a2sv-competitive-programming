class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for row in range(rows):
            curr_row = row + 1
            curr_col = 1
            while curr_row < rows and curr_col < cols:
                if matrix[curr_row][curr_col] != matrix[curr_row - 1][curr_col - 1]:
                    return False
                curr_row += 1
                curr_col += 1
        
        for col in range(cols):
            curr_row = 1
            curr_col = col + 1
            while curr_row < rows and curr_col < cols:
                if matrix[curr_row][curr_col] != matrix[curr_row - 1][curr_col - 1]:
                    return False
                curr_row += 1
                curr_col += 1
        
        return True
        