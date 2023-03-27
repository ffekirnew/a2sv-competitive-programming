class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0
        deletions = []
        
        for row in grid:
            row.sort()
            
        for deletion in range(len(grid[0])):
            deletions.append([])

            for row in grid:
                deletions[-1].append(row.pop())
            
            print(deletions)
            answer += max(deletions[-1])
        
        return answer
        