class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        
        for row in grid:
            row.sort()
            answer += bisect_left(row, 0)
        
        return answer
        