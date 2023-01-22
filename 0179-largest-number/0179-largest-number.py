class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # change all elements to strings
        nums = list(map(str, nums))
        
        # use insertion sort to find the minimum number
        for idx in range(len(nums) - 1):
            swap_idx = idx + 1
            
            while swap_idx > 0 and nums[swap_idx] + nums[swap_idx - 1] < nums[swap_idx - 1] + nums[swap_idx]:
                nums[swap_idx], nums[swap_idx - 1] = nums[swap_idx - 1], nums[swap_idx] 
                swap_idx -= 1
        
        # clean multiple zeros
        while len(nums) > 1 and nums[-2] == nums[-1] == "0":
            nums.pop()
        
        return "".join(reversed(nums))
                
        