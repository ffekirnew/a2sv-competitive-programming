class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = []
        
        for r, row in enumerate(matrix):
            self.prefix_sum.append([])
            
            for c, cell in enumerate(row):
                # initialized
                pf_before = self.prefix_sum[r][c-1] if c > 0 else 0
                pf_above = self.prefix_sum[r-1][c] if r > 0 else 0
                pf_diagonal = self.prefix_sum[r-1][c-1] if r > 0 and c > 0 else 0
                
                formula = cell + pf_before + pf_above - pf_diagonal
                
                self.prefix_sum[-1].append(formula)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        all_sum = self.prefix_sum[row2][col2]
        left_sum = self.prefix_sum[row2][col1 - 1] if col1 > 0 else 0
        top_sum = self.prefix_sum[row1 - 1][col2] if row1 > 0 else 0
        
        tobe_added_sum = self.prefix_sum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        
        return all_sum - left_sum - top_sum + tobe_added_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)