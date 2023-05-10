import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        queue = [(matrix[0][0], 0, 0)]
        DIRS = [[0, 1], [1, 0]]
        
        def in_bound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        
        visited = set()
        while queue:
            number, row, col = heapq.heappop(queue)
            k -= 1

            if not k:
                return number
            
            for r, c in DIRS:
                nx_row, nx_col = row + r, col + c
                
                if in_bound(nx_row, nx_col) and (nx_row, nx_col) not in visited:
                    visited.add((nx_row, nx_col))
                    heapq.heappush(queue, (matrix[nx_row][nx_col], nx_row, nx_col))
                
                
            
            
            
        