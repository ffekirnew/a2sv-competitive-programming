class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(index: int, pass_start: int, curr_ticket: int):
            if index == len(days):
                return 0
            
            if curr_ticket is not None and days[index] - days[pass_start] < curr_ticket:
                return dp(index + 1, pass_start, curr_ticket)
            
            return min(
                    costs[0] + dp(index + 1, index, 1),
                    costs[1] + dp(index + 1, index, 7),
                    costs[2] + dp(index + 1, index, 30)
                )
        
        return dp(index = 0, pass_start = -1, curr_ticket = None)

