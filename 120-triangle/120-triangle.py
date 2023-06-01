class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(row, col, path_sum):
            if row == len(triangle):
                return path_sum
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            left_path_sum = dp(row + 1, col, 0)
            right_path_sum = dp(row + 1, col + 1, path_sum + 0)
            
            
            memo[(row, col)] = triangle[row][col] + min(left_path_sum, right_path_sum)
            return memo[(row, col)]
        
        return dp(0, 0, 0)
        