class Solution:
    def findPrefixSum(self, matrix: List[List[int]]):
        prefix_sum = []
        for r, row in enumerate(matrix):
            prefix_sum.append([])

            for c, cell in enumerate(row):
                pf_before = prefix_sum[r][c-1] if c > 0 else 0
                pf_above = prefix_sum[r-1][c] if r > 0 else 0
                pf_diagonal = prefix_sum[r-1][c-1] if r > 0 and c > 0 else 0

                pf_cell = cell + pf_before + pf_above - pf_diagonal

                prefix_sum[-1].append(pf_cell)

        return prefix_sum

    def sumRegion(self, prefix_sum: List[List[int]], row1: int, col1: int, row2: int, col2: int) -> int:
        rows, cols = len(prefix_sum), len(prefix_sum[0])
        
        all_sum = prefix_sum[row2][col2] if row2 < rows and col2 < cols else 0

        left_sum = prefix_sum[row2][col1 - 1] if 0 < col1 and row2 < rows else 0
        top_sum = prefix_sum[row1 - 1][col2] if 0 < row1 and col2 < cols else 0
        
        tobe_added_sum = prefix_sum[row1 - 1][col1 - 1] if 0 < row1 and 0 < col1 else 0
        
        return all_sum - left_sum - top_sum + tobe_added_sum

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix_sum = self.findPrefixSum(mat)
        rows, cols = len(prefix_sum), len(prefix_sum[0])
        
        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                row1, col1 = r - k, c - k
                row2 = r + k if r + k < rows else rows - 1 
                col2 = c + k if c + k < cols else cols - 1 
                mat[r][c] = self.sumRegion(prefix_sum, row1, col1, row2, col2)
        
        return mat
            
        