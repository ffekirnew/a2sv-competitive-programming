class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # create the object to be returned
        answer = [[], []]
        # count all players and losers
        players = set()
        losers = {}
        for match in matches:
            players.add(match[0])
            players.add(match[1])
            losers[match[1]] = losers.get(match[1], 0) + 1
            
        players = list(players)
        players.sort()
        
        for player in players:
            if losers.get(player, 0) == 0:
                answer[0].append(player)
            elif losers.get(player, 0) == 1:
                answer[1].append(player)
        # return the solution
        return answer