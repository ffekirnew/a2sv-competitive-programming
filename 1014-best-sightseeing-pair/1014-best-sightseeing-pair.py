class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = {}
        dp[1] = [
            values[0] - 1,
            values[1]
        ]
        best = values[0] + values[1] - 1
        
        for i in range(2, len(values)):
            best_at_last_index = max(dp[i - 1]) - 1
            best = max(best, best_at_last_index + values[i])
            
            dp[i] = [
                best_at_last_index,
                values[i]
            ]
        
        return best