class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        prefix_grid = [ [0] * (n + 1) for i in range(n + 1) ]
        
        for query in queries:
            prefix_grid[query[0]][query[1]] += 1
            prefix_grid[query[0]][query[3] + 1] -= 1
            prefix_grid[query[2] + 1][query[1]] -= 1
            prefix_grid[query[2] + 1][query[3] + 1] += 1
        
        for r, row in enumerate(prefix_grid):
            for c, col in enumerate(row):
                cell = prefix_grid[r][c]
                pf_above = prefix_grid[r - 1][c] if r > 0 else 0
                pf_before = prefix_grid[r][c - 1] if c > 0 else 0
                pf_diagonal = prefix_grid[r - 1][c - 1] if c > 0 and r > 0 else 0
                
                prefix_grid[r][c] = cell + pf_above + pf_before - pf_diagonal
        
        prefix_grid.pop()
        
        for row in prefix_grid:
            row.pop()
        
        return prefix_grid