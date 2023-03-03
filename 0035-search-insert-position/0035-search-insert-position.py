class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = bisect_left( nums, target, 0, len(nums) - 1 )
        if pos == len(nums) - 1 and nums[pos] < target:
            return pos + 1
        return pos
            