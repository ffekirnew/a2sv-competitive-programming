class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # sort both arrays
        players.sort()
        trainers.sort()
        
        # create the object to be returned
        answer = 0
        
        # loop through the arrays
        i, j = 0, 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                answer += 1
                i += 1
                j += 1
            else:
                j += 1
                
        # return the solution
        return answer
        