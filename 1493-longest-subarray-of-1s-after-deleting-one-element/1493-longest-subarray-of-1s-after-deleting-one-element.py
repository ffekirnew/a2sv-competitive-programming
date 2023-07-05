class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0

        zeros_encountered = 0
        left = 0
        
        for right in range(len(nums)):
            zeros_encountered += int(nums[right] == 0)
            
            while zeros_encountered > 1:
                zeros_encountered -= int(nums[left] == 0)
                left += 1
            
            longest = max(longest, right - left)
        
        return longest
        