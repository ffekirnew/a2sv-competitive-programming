from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_subarray_sum = 0
        
        # set up the sliding window
        window_frequency_count = {}
        def count_frequency(number: int) -> None:
            window_frequency_count[number] = window_frequency_count.get(number, 0)
            window_frequency_count[number] += 1
        
        def remove_frequency(number: int) -> None:
            window_frequency_count[number] -= 1
            if window_frequency_count[number] == 0:
                del window_frequency_count[number]

        window_sum = 0

        left = 0
        for right, number in enumerate(nums):
            count_frequency(number)
            window_sum += number
            
            if right - left + 1 > k:
                remove_frequency(nums[left])
                window_sum -= nums[left]
                left += 1
            
            if right - left + 1 == k and len(window_frequency_count) == right - left + 1:
                max_subarray_sum = max(window_sum, max_subarray_sum)
            
        
        return max_subarray_sum
        