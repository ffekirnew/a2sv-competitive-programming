class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def predict(l: int, r: int) -> int:
            if l > r:
                return 0
            
            if_right_taken = nums[r] - predict(l, r - 1)
            if_left_taken = nums[l] - predict(l + 1, r)
            
            return max( if_right_taken, if_left_taken )
        
        return predict( 0, len(nums) - 1 ) >= 0
        
        
            
        