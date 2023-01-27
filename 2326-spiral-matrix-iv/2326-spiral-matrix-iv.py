# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1 for i in range(n)] for j in range(m)]
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr_dir = 0
        
        curr_row = 0
        curr_col = 0
        
        visited = set()
        
        while head:
            if (0 <= curr_row < m) and (0 <= curr_col < n) and tuple([curr_row, curr_col]) not in visited:
                result[curr_row][curr_col] = head.val
                visited.add(tuple([curr_row, curr_col]))
                
                curr_row += directions[curr_dir][0]
                curr_col += directions[curr_dir][1]
                head = head.next
                
            else:
                curr_row -= directions[curr_dir][0]
                curr_col -= directions[curr_dir][1]
                
                curr_dir = (curr_dir + 1) % 4
                
                curr_row += directions[curr_dir][0]
                curr_col += directions[curr_dir][1]
        
        return result