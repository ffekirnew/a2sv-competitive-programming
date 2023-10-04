"""
Solution Steps:
1. Initialize return variable and sliding window
2. Loop over the list using the right edge and move it one at a time
    2.1. If the current number pointed at by right can be added to the running subarray, add it
    2.2. If not, try moving the left pointer
"""


class CountSubarraysWithScoreLessThanK:
    def sliding_window_solution(self, nums: List[int], k: int) -> int:
        count = 0
        
        # do something
        running_sum = 0
        left = 0
        for right, number in enumerate(nums):
            while (number + running_sum) * (right - left + 1) >= k:
                running_sum -= nums[left]
                left += 1

            count += (right - left + 1)
            running_sum += number
        
        return count

    
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        solution = CountSubarraysWithScoreLessThanK()
        return solution.sliding_window_solution(nums, k)
        