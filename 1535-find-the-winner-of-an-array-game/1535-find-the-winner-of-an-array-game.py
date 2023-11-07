"""
Notes:
- game between elements 0 and 1

Solution Steps:
1. Initialize a winner variable
2. Initialize palyer1 and player2, and win_streak variable
3. Loop throught the array
    3.1. Check the winner, if winner is new, win_streak becomes 1
    3.2. if winner is old, update win_streak by 1
    3.3. if win_streak is k, break
n. Return winner
"""
class FindTheWinnerOfAnArrayGame:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
    
    def approach_1(self):
        if self.k > len(self.arr):
            return max(self.arr)

        winner = None
        player_1_index, player_2_index = 0, 1
        win_streak = 0
        
        while win_streak < self.k:
            if self.arr[player_1_index] < self.arr[player_2_index]:
                if winner == self.arr[player_2_index]:
                    win_streak += 1
                else:
                    win_streak = 1
                    winner = self.arr[player_2_index]

            else:
                if winner == self.arr[player_1_index]:
                    win_streak += 1
                else:
                    win_streak = 1
                    winner = self.arr[player_1_index]

                self.arr[player_1_index], self.arr[player_2_index] = self.arr[player_2_index], self.arr[player_1_index]

            player_1_index = (player_1_index + 1) % len(self.arr)
            player_2_index = (player_2_index + 1) % len(self.arr)
        
        return winner


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        solution = FindTheWinnerOfAnArrayGame(arr, k)
        return solution.approach_1()
        