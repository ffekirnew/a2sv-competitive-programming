class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        range_ = max(nums) - min(nums)
        return max(range_ - 2 * k, 0)
        
        
        