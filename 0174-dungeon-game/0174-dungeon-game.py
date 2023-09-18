class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        
        def dp(row: int, col: int) -> int:
            if not ( 0 <= row < ROWS and 0 <= col < COLS ):
                return inf
            
            return dungeon[row][col]
        
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if row == ROWS - 1 and col == COLS - 1:
                    dungeon[row][col] = max(1, 1 - dungeon[row][col])

                else:
                    right = max(1, dp(row, col + 1) - dungeon[row][col])
                    down = max(1, dp(row + 1, col) - dungeon[row][col])
                    
                    dungeon[row][col] = min(right, down)
        

        return dungeon[0][0]