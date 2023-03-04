class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 1
        
        tickets = deque([ [val, idx] for idx, val in enumerate(tickets) ])
        
        while tickets:
            curr = tickets.popleft()
            
            if curr[0] == 1 and curr[1] == k:
                return time
            
            if curr[0] > 1:
                tickets.append([curr[0] - 1, curr[1]])

            time += 1
        
        return time