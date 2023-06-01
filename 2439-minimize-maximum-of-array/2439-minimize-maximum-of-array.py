class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        running_sum = 0
        
        answer = -inf
        
        for r in range(len(nums)):
            running_sum += nums[r]
            answer = max(math.ceil(running_sum / (r + 1)), answer) 
        
        return answer
            
                
        