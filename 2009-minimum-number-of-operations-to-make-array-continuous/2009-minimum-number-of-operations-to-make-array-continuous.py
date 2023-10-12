"""
Solution Steps:
1. Sort the array
2. Count the gaps
3. Return the number of gaps

Complexity Analysis:
- Time Complexity: O(nlogn)
- Space Complexity: O(1)
"""
from typing import List
from bisect import bisect_right
from math import inf


class MinimumNumberOfOperationsToMakeArrayContinuous:
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def minimum_operations(self) -> int:
        min_ops = inf
        
        n = len(self.nums)
        nums = sorted(list(set(self.nums)))
        
        for i, num in enumerate(nums):
            included = bisect_right(nums, num + n - 1) - i
            
            min_ops = min(min_ops, n - included)
            
        return min_ops
                

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        solution = MinimumNumberOfOperationsToMakeArrayContinuous(nums)
        return solution.minimum_operations()
        