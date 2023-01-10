class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # create variables to hold the length and height of the matrix
        row = len(matrix)
        col = len(matrix[0])
        # create the object to be returned
        answer = []
        # create a hashmap to keep track of the already visited rows
        rows = {}
        columns = {}
        # create direction guides
        directions = ['r', 'd', 'l', 'u']
        curr_direction = directions[0]
        # create a variable to aid in the looping
        i, j = 0, 0
        while len(rows.keys()) <= len(matrix):
            print(answer)
            print("rows:", rows, "columns:", columns)
            answer.append(matrix[i][j])
            if curr_direction == 'r':
                next_col = j + 1
                if next_col in columns or next_col == col:
                    next_row = i + 1
                    if next_row in rows or next_row == row: 
                        break
                    else: 
                        rows[i] = 1
                        i = next_row
                        curr_direction = 'd'
                else:
                    j = next_col
            elif curr_direction == 'd':
                print(i)
                next_row = i + 1
                if next_row in rows or next_row == row:
                    print("i am here")
                    next_col = j - 1
                    if next_col in columns or next_col == -1: 
                        break
                    else:
                        columns[j] = 1
                        j = next_col
                        curr_direction = 'l'
                else:
                    i = next_row
            elif curr_direction == 'l':
                next_col = j - 1
                if next_col in columns or next_col == -1:
                    next_row = i - 1
                    if next_row in rows or next_row == -1: 
                        break
                    else:
                        rows[i] = 1
                        i = next_row
                        curr_direction = 'u'
                else:
                    j = next_col
            else:
                next_row = i - 1
                if next_row in rows or next_row == -1:
                    next_col = j + 1
                    if next_col in columns or next_col == col: 
                        break
                    else:
                        columns[j] = 1
                        j = next_col
                        curr_direction = 'r'
                else:
                    i = next_row
            
                    
        # return the object
        return answer