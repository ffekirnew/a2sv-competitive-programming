class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}
        def dp(index, first_house_robbed=None):
            if index == 0:
                return max(dp(index + 2, True) + nums[index], dp(index + 1, False))

            if index >= len(nums):
                return 0

            if index == len(nums) - 1:
                return 0 if first_house_robbed else nums[index]
            
            if (index, first_house_robbed) not in memo:
                memo[(index, first_house_robbed)] = max(dp(index + 2, first_house_robbed) + nums[index], dp(index + 1, first_house_robbed))
            
            return memo[(index, first_house_robbed)]
        
        return dp(0)
            
        
        