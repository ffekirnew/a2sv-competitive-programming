class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        def is_possible(r, c):
            for row in range(n):
                for col in range(n):
                    if grid[row][col] == 'Q':
                        if row == r or col == c or row - col == r - c or row + col == r + c:
                            return False

            return True

        def solve(row = 0):
            if row == n:
                answer[0] += 1
                return

            for y in range(n):
                if is_possible(row, y):
                    grid[row][y] = 'Q'
                    solve(row + 1)
                    grid[row][y] = '.'

        answer = [0]
        solve()
        return answer[0]
                            
                    
            
        
        