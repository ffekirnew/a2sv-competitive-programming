class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        zero_cont_rows = []
        zero_cont_cols = []
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_cont_rows.append(row)
                    zero_cont_cols.append(col)
        
        for row in zero_cont_rows:
            for col in range(cols):
                matrix[row][col] = 0
        
        for col in zero_cont_cols:
            for row in range(rows):
                matrix[row][col] = 0
        