class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(index: int, choices_left: int):
            if index == len(piles) or choices_left == 0:
                return 0
            
            max_piles = dp(index + 1, choices_left)
            chosen = 0
            for i in range(min(choices_left, len(piles[index]))):
                chosen += piles[index][i]
                max_piles = max(chosen + dp(index + 1, choices_left - i - 1), max_piles)
            
            return max_piles
        
        return dp(0, k)
                
                
        