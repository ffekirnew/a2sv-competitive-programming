from collections import defaultdict

class MaximumSumOfDistinctSubarraysWithLengthK:
    def __init__(self, nums: List[int], k: int):
        self.nums = nums
        self.k = k
        
    def _set_up(self):
        self.window_frequency_count = {}

    def _count_frequency(self, number: int) -> None:
        self.window_frequency_count[number] = self.window_frequency_count.get(number, 0)
        self.window_frequency_count[number] += 1

    def _remove_frequency(self, number: int) -> None:
        self.window_frequency_count[number] -= 1
        if self.window_frequency_count[number] == 0:
            del self.window_frequency_count[number]
    
    def solve(self):
        max_subarray_sum = 0

        self._set_up()
        window_sum = 0
        left = 0
        for right, number in enumerate(self.nums):
            self._count_frequency(number)
            window_sum += number
            
            if right - left + 1 > self.k:
                self._remove_frequency(self.nums[left])
                window_sum -= self.nums[left]
                left += 1
            
            if right - left + 1 == self.k and len(self.window_frequency_count) == right - left + 1:
                max_subarray_sum = max(window_sum, max_subarray_sum)
        
        return max_subarray_sum


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        solution = MaximumSumOfDistinctSubarraysWithLengthK(nums, k)
        return solution.solve()
        