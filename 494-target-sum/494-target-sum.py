class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def solve(index, curr_sum):
            if index == len(nums):
                return curr_sum == target
            
            answer = 0
            answer += solve(index + 1, curr_sum + nums[index])
            answer += solve(index + 1, curr_sum - nums[index])
            
            return answer
        
        return solve(0, 0)
                
        