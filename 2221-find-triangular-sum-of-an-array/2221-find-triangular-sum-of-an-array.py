class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            next_nums = [0] * (len(nums) - 1)
            
            for i in range(len(next_nums)):
                next_nums[i] = (nums[i] + nums[i + 1]) % 10
            
            nums = next_nums
        
        return nums[0]
        