class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        nums = deque(nums)
        
        while nums and nums[0] <= 0:
            nums.popleft()
        
        prev = 0
        while nums and nums[0] - prev <= 1:
            prev = nums.popleft()
        
        return prev + 1
        