class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        
        while i < len(nums):
            if nums[i] == i + 1 or nums[nums[i] - 1] == nums[i]:
                i += 1
            else:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        
        answer = []
        
        for i, num in enumerate(nums):
            if num != i + 1:
                return [num, i + 1]