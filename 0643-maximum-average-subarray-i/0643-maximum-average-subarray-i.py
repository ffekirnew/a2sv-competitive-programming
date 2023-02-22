class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        start = 0
        
        curr_sum = 0
        
        for end in range(len(nums)):
            curr_sum += nums[end]
            
            if end - start >= k - 1:
                max_sum = max( max_sum, curr_sum )
                curr_sum -= nums[start]
                start += 1
        
        return max_sum / k
        