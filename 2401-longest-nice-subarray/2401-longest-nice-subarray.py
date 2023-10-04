"""
Solution Steps:
1. Set up the sliding window
2. Move the right end of the window one at a time
    2.1. Oring them with running number
    2.2. If the current or of numbers & number at right end is zero, move the left
    2.3. Maximize longest window
3. Return the solution

Complexity Analysis:
- Time Complexity: 
- Space complexity: 
"""

class LongestNiceSubarray:
    def sliding_window(self, nums: List[int]) -> int:
        longest_nice_subarray = 0
        
        curr_or = 0
        left = 0
        for right, num in enumerate(nums):
            while curr_or & num:
                curr_or -= nums[left]
                left += 1
            
            curr_or += num
            longest_nice_subarray = max(longest_nice_subarray, right - left + 1)
        
        return longest_nice_subarray


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        solution = LongestNiceSubarray()
        return solution.sliding_window(nums)
        