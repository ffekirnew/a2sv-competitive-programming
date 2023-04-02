class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtrack(curr_or, index):
            if curr_or:
                or_values.append(curr_or)
                
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                backtrack(curr_or | nums[i], i + 1)
            
        or_values = []
        # do backtracking
        backtrack(0, 0)
        
        return max([ (key, value) for key, value in Counter(or_values).items() ])[1]
        