class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # change all consec. numbers based on the formula
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i - 1] *= 2
                nums[i] = 0
        
        # move all zeros to the back
        read, write = 0, 0
        while read < len(nums):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
            
            read += 1
        
        return nums
        