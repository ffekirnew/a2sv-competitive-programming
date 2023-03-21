class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subarrays = 0
        
        l, r = 0, 0
        
        while r < len(nums):
            while l < len(nums) and nums[l]:
                l += 1
            
            while r < l:
                r += 1
            
            while l < len(nums) and r < len(nums) and nums[l] == nums[r] == 0:
                subarrays += r - l + 1
                r += 1
            
            l = r
        
        return subarrays
        