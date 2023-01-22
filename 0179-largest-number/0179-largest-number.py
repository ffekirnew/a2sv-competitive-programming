class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        for idx in range(len(nums) - 1):
            swap_idx = idx + 1
            
            while swap_idx > 0 and nums[swap_idx] + nums[swap_idx - 1] < nums[swap_idx - 1] + nums[swap_idx]:
                nums[swap_idx], nums[swap_idx - 1] = nums[swap_idx - 1], nums[swap_idx] 
                swap_idx -= 1
        
        while len(nums) > 1 and nums[-2] == nums[-1] == "0":
            nums.pop()
        
        return "".join(reversed(nums))
                
        