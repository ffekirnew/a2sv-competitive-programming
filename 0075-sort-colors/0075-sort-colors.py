class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        
        idx = 0
        
        for zero in range(count.get(0, 0)):
            nums[idx] = 0
            idx += 1
        
        for one in range(count.get(1, 0)):
            nums[idx] = 1
            idx += 1
        
        for two in range(count.get(2, 0)):
            nums[idx] = 2
            idx += 1
        