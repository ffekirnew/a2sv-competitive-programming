class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_arr):
            if len(curr_arr) == len(nums):
                answer.append(curr_arr)
                
            
            for i in range(len(nums)):
                if nums[i] not in curr_arr:
                    backtrack(curr_arr + [nums[i]])
            
        answer = []
        backtrack([])
        return answer
        