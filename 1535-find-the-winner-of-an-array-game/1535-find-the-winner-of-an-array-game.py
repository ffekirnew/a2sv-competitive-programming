class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        
        player1, player2 = 0, 1
        win_streak = 0
        winner = None
        
        while win_streak < k:
            round_winner = arr[player1] if arr[player1] > arr[player2] else arr[player2]
            
            if arr[player1] > arr[player2]:
                arr[player1], arr[player2] = arr[player2], arr[player1]

            if winner != round_winner:
                winner = round_winner
                win_streak = 0
            
            win_streak += 1
            
            player1 = (player1 + 1) % len(arr)
            player2 = (player2 + 1) % len(arr)
        
        return winner
        
        
        