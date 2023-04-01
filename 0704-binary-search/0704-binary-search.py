class Solution:
    def search(self, nums: List[int], target: int) -> int:
        place = bisect_left(nums, target)
        
        if place < len(nums) and nums[place] == target:
            return place
        return -1
        