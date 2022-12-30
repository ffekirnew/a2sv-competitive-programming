class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # give variables for rows and columns
        rows = len(grid)
        cols = len(grid[0])
        
        # create the object to be returned
        answer = []
        
        # find row and column ones and zeros
        row_zeros_ones = defaultdict(dict)
        col_zeros_ones = defaultdict(dict)
        for row in range(rows):
            for col in range(cols):
                row_zeros_ones[row][grid[row][col]] = row_zeros_ones[row].get(grid[row][col], 0) + 1
                col_zeros_ones[col][grid[row][col]] = col_zeros_ones[col].get(grid[row][col], 0) + 1

        # fill the answers
        for row in range(rows):
            answer.append([])
            for col in range(cols):
                diff = row_zeros_ones[row].get(1, 0) + col_zeros_ones[col].get(1, 0)
                diff -= row_zeros_ones[row].get(0, 0) + col_zeros_ones[col].get(0, 0)
                answer[-1].append(diff)
                
        
        # return the solution
        return answer
        