class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        
        dirs = [ [1, 0], [0, 1], [-1, 0], [0, -1] ]
        in_bound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        
        def dfs(row: int, col: int, start_color: int):
            stack = [tuple([row, col,])]
            visited = set()
            
            while stack:
                cr, cc = stack.pop()
                image[cr][cc] = color
                
                visited.add(tuple([cr, cc]))
            
                for next_row, next_col in dirs:
                    ncr = cr + next_row
                    ncc = cc + next_col
                    

                    if (tuple([ncr, ncc]) not in visited) and in_bound(ncr, ncc) and image[ncr][ncc] == start_color:
                        stack.append(tuple([ncr, ncc]))
                        
        dfs(sr, sc, image[sr][sc])
        
        return image
        
        
        