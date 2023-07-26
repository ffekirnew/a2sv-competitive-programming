class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        sum_ending_at_last_index = {1: satisfaction[0]}
        max_sum = max(satisfaction[0], 0)
        
        for i in range(1, len(satisfaction)):
            num = satisfaction[i]
            sum_ending_at_index = {1: num}
            max_sum  = max(max_sum, num)
            
            for length in range(1, i + 1):
                sum_ending_at_index[length + 1] = sum_ending_at_last_index[length] + (num * (length + 1))
                max_sum = max(max_sum, sum_ending_at_index[length + 1])
            
            sum_ending_at_last_index = sum_ending_at_index
        
        return max_sum
                    
                
        