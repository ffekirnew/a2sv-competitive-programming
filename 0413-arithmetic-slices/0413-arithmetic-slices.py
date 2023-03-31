class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        subarrays = 0
        
        l, r = 0, 1
        difference = nums[r] - nums[l]
        
        while r < len(nums):
            if nums[r] - nums[r - 1] != difference:
                l = r - 1
                difference = nums[r] - nums[r - 1]
            
            if r - l >= 2:
                subarrays += r - l - 1
            
            r += 1
        
        return subarrays