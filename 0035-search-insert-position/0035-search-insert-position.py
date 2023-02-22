class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        curr = 0
        
        while curr < len(nums):
            if nums[curr] == target:
                return curr
            elif nums[curr] > target:
                break
            curr += 1
        
        return curr
            