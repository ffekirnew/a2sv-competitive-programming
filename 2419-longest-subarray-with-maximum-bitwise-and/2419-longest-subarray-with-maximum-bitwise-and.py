class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_number = max(nums)
        max_length = 1
        
        l = 0
        for r in range(len(nums)):
            if nums[r] != nums[l] or nums[l] != max_number:
                l = r
            
            max_length = max(max_length, r - l + 1)
        
        return max_length
                
        