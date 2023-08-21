class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        
        max_ = -inf
        for i in range(1, len(nums)):
            max_ = max(max_, nums[i] - nums[i - 1])
        
        return max_
        