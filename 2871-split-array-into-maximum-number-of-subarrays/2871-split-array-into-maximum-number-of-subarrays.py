class SplitArrayIntoMaximumNumberOfSubarrays:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def solve(self):
        zero_subarrays_counter = 0
        running_and = ~0
        
        for num in self.nums:
            running_and &= num
            
            if running_and == 0:
                zero_subarrays_counter += 1
                running_and = ~0
        
        return max(zero_subarrays_counter, 1)


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        solution = SplitArrayIntoMaximumNumberOfSubarrays(nums)
        return solution.solve()
        
        
        
