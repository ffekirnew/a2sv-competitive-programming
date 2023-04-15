class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # find all islands in grid2
        grid2_islands = []
        
        # helper function to know if a certain row, col is inbound
        in_bound = lambda row, col: 0 <= row < len(grid2) and 0 <= col < len(grid2[0])
        
        # the directions we can move in
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        # helper function to do dfs
        def dfs(row, col):
            grid2[row][col] = 0
            grid2_islands[-1].append(tuple([row, col,]))
            
            for next_row, next_col in dirs:
                new_row = row + next_row
                new_col = col + next_col
                
                if in_bound(new_row, new_col) and grid2[new_row][new_col]:
                    dfs(new_row, new_col)
        
        # count all islands
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]:
                    grid2_islands.append([])
                    dfs(i, j)
        
        # create the objects to be returned
        answer = 0
        
        # if all islands in grid2_islands exists wholly in grid1, count them
        for island in grid2_islands:
            answer += all( grid1[row][col] == 1 for row, col in island )
        
        return answer
        