class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # rows and cols for simplicity
        rows = len(matrix)
        cols = len(matrix[0])
        
        # create the obect to be returned
        answer = []
        
        
        # specify the directions to go at
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        # store the current direction:
        curr_dir = 0
        
        # store the current location
        curr_loc = [0, -1]
        
        total = rows * cols
        
        # loop through the matrix
        i = 0
        while i < total:
            next_loc = [curr_loc[0] + directions[curr_dir][0], curr_loc[1] + directions[curr_dir][1]]
            
            if 0 <= next_loc[0] < rows and 0 <= next_loc[1] < cols and matrix[next_loc[0]][next_loc[1]] != 101:
                answer.append(matrix[next_loc[0]][next_loc[1]])
                matrix[next_loc[0]][next_loc[1]] = 101
                curr_loc = next_loc
                i += 1
            else:
                curr_dir = (curr_dir + 1) % 4
        
        return answer