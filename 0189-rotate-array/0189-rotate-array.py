class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        auxiliary = []
        
        boundary = len(nums) - k

        while boundary >= len(nums):
            boundary -= len(nums)
        while boundary < -1 * len(nums):
            boundary += len(nums)

        for idx in range( boundary, len(nums) ):
            auxiliary.append(nums[idx])
        
        for idx in range( boundary ):
            auxiliary.append(nums[idx])
            
        for idx in range(len(nums)):
            nums[idx] = auxiliary[idx]