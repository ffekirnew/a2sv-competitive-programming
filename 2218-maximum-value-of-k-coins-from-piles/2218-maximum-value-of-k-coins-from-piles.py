class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(index: int, choices_left: int) -> int:
            if index == len(piles) or choices_left == 0:
                return 0
            
            # not picking from this pile and delegating the responsibility
            optimal_choice = dp(index + 1, choices_left)

            # Incrementally optimize by mixing choices between different piles
            chosen_from_this_pile = 0
            for i in range(min(choices_left, len(piles[index]))):
                chosen_from_this_pile += piles[index][i]
                new_choice = chosen_from_this_pile + dp(index + 1, choices_left - i - 1)
                
                optimal_choice = max(new_choice, optimal_choice)
            

            return optimal_choice
        
        return dp(0, k)
                
                
        