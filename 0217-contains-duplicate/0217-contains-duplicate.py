class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort nums
        nums.sort()
        
        # look if contiguous values are equal
        for index in range(1, len(nums)):
            if nums[index - 1] == nums[index]:
                return True
        return False
        