class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)

        @cache
        def dp(index: int, group_1: int) -> int:
            if index == len(stones):
                return abs(group_1 - abs(total_sum - group_1))
            
            return min(dp(index + 1, group_1 + stones[index]), dp(index + 1, group_1))
        
        return dp(0, 0)
            
            
