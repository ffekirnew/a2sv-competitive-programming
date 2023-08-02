class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [["" for _ in range(len(s))] for __ in range(numRows)]
        
        def check_in_bound(row, col):
            return 0 <= row < len(rows) and 0 <= col < len(s)
        
        direction = 1 # 0 for down 1 for up
        can_go = [[1, 0], [-1, 1]]

        curr_row, curr_col = -1, 0
        for char in s:
            if not check_in_bound(curr_row + can_go[direction][0], curr_col + can_go[direction][1]):
                direction = 1 - direction
            correct_cell = curr_row + can_go[direction][0], curr_col + can_go[direction][1]
            curr_row, curr_col = correct_cell

            rows[curr_row][curr_col] = char
        
        order = []
        for row in range(numRows):
            for col in range(len(s)):
                if rows[row][col]:
                    order.append(rows[row][col])
        
        return "".join(order)
                
            
            
        