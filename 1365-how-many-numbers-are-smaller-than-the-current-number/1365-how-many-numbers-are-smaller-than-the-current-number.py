class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        
        for i in range(length):
            for j in range(length):
                if nums[i] > nums[j]:
                    result[i] += 1
        
        return result