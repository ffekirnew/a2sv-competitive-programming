class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        suffix_sum = [0] * len(grid[0])
        prefix_sum = [0] * len(grid[0])
        
        prefix = suffix = 0
        for i in range(len(prefix_sum)):
            prefix_sum[i] = prefix
            prefix = grid[1][i] + prefix_sum[i]
            
            suffix_sum[len(suffix_sum) - i - 1] = suffix
            suffix = grid[0][len(suffix_sum) - i - 1] + suffix_sum[len(suffix_sum) - i - 1]
            
            
        #Want the lowest of the worst-case scenerio.
        #Player 2 will attempt to pick the biggest of prefix_sum[i] or suffix_sum[i].
        #Player 1 will attempt to pick the case that will minimize this.
        lowest = float("inf")
        for i in range(len(prefix_sum)):
            lowest = min(lowest, max(prefix_sum[i], suffix_sum[i]))
            
        return lowest
