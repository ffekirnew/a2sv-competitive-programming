class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix)
        
        
        # transpose the matrix
        for row in range(rows):
            for col in range(row, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                
        # reverse each row of the matrix
        for row in range(rows):
            for idx in range(cols // 2):
                matrix[row][idx], matrix[row][cols - idx - 1] = matrix[row][cols - idx - 1], matrix[row][idx]
        