class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        # create the object to be returned
        ans = 0
        # find the prefix sums for the matrix
        p = []
        for row in range(len(grid)):
            p.append([])
            for column in range(len(grid[row])):
                if not column:
                    p[-1].append(grid[row][column])
                else:
                    p[-1].append(p[row][-1] + grid[row][column])
        # add the hour glasses
        rows, cols = len(grid), len(grid[0])
        i = 0
        for i in range(rows - 2):
            for j in range(2, cols):
                curr = p[i][j] + p[i + 2][j] + grid[i + 1][j - 1]
                if j - 3 >= 0:
                    curr -= p[i][j - 3]
                    curr -= p[i + 2][j - 3]
                ans = max(curr, ans)
        # return the solution
        return ans