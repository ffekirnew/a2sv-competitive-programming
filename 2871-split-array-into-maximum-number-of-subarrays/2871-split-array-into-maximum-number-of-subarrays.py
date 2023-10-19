class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        minimum_and = reduce(lambda x, y: x & y, nums)
        
        if minimum_and:
            return 1
        
        counter = 0
        running_and = ~0
        
        for num in nums:
            running_and &= num
            
            if running_and == 0:
                counter += 1
                running_and = ~0
        
        return counter
        
        
        
