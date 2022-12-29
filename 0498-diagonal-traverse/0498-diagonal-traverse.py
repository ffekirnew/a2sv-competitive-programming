class Solution:            
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # store the rows and columns
        rows = len(mat)
        cols = len(mat[0])
        
        # create the object to be returned
        answer = []
        
        # generate all diagonals and store them
        diagonals = defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                diagonals[row + col].append(mat[row][col])
        
        # loop through the diagonals and append the answers
        forward = False
        for diagonal in diagonals.values():
            if forward:
                for number in diagonal:
                    answer.append(number)
            else:
                for number in reversed(diagonal):
                    answer.append(number)
            forward = not forward
        
        # return the solution
        return answer
        