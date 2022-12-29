class Solution:            
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # store the rows and columns
        rows = len(mat)
        cols = len(mat[0])
        
        # create the object to be returned
        answer = []
        
        # generate all diagonals and store them
        diagonals = []
        for i in range(rows):
            diagonals.append([])
            row, col = i, 0
            while row > -1 and col <  cols:
                diagonals[-1].append(mat[row][col])
                row -= 1
                col += 1
        diagonals.pop()
        for j in range(cols):
            diagonals.append([])
            row, col = i, j
            while row > -1 and col <  cols:
                diagonals[-1].append(mat[row][col])
                row -= 1
                col += 1
            
        
        # loop through the diagonals and append the answers
        forward = True
        for diagonal in diagonals:
            if forward:
                for number in diagonal:
                    answer.append(number)
            else:
                for number in reversed(diagonal):
                    answer.append(number)
            forward = not forward
        
        # return the solution
        return answer
        