class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 0
        
        memo = {0: 1}
        def dp(target):
            if target < 0:
                return 0

            if target not in memo:
                memo[target] = 0
                for num in nums:
                    memo[target] += dp(target - num)
            
            return memo[target]
        
        return dp(target)
                    
                
        