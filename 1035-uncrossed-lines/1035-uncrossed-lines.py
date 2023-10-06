"""
Solution Steps:
The problem is asking for the common subsequence between the two
1. Using DP look for the most common and longest subsequence between them

Complexity Analysis:
- Time Complexity: O(n**2)
- Space Complexity: O(n ** 2) - For the function call stack
"""


class UncrossedLines:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
    
    def top_down(self):
        @cache
        def dp(index1: int, index2: int) -> int:
            if index1 == len(self.nums1) or index2 == len(self.nums2):
                return 0
            
            if self.nums1[index1] == self.nums2[index2]:
                return 1 + dp(index1 + 1, index2 + 1)

            return max(dp(index1 + 1, index2), dp(index1, index2 + 1))
        
        return dp(0, 0)


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        solution = UncrossedLines(nums1, nums2)
        return solution.top_down()
        