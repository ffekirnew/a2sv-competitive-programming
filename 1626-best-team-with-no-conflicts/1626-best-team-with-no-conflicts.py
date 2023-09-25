class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores_and_ages = [(ages[i], scores[i]) for i in range(len(scores))]
        scores_and_ages.sort()
        
        @cache
        def dp(index: int, highest_so_far: int) -> int:
            if index == len(scores_and_ages):
                return 0
            
            age, score = scores_and_ages[index]
            highest_score_age, highest_score = highest_so_far

            if highest_score > score and highest_score_age < age:
                return dp(index + 1, highest_so_far)
            
            else:
                highest_possible = dp(index + 1, highest_so_far)
                
                if score >= highest_score:
                    highest_possible = max(highest_possible, score + dp(index + 1, (age, score)))
                else:
                    highest_possible = max(highest_possible, score + dp(index + 1, (highest_score_age, highest_score)))
                
                return highest_possible
           
        return dp(0, (0, 0))
 