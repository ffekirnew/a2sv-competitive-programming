class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = set()
        
        def backtrack(curr, curr_indices):
            if len(curr) == len(nums):
                permutations.add(tuple(curr))
                return
            
            for i, num in enumerate(nums):
                if i not in curr_indices:
                    backtrack(curr + [num], curr_indices + [i])
        
        backtrack([], [])
        return permutations
        