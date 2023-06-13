import sys
sys.setrecursionlimit(1_000_000)

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # top down approach
        memo = {}
        def dp(index):
            if index in memo:
                return memo[index]
            
            if index >= len(questions):
                return 0
            
            do_this = questions[index][0]
            if (index + questions[index][1] + 1) < len(questions):
                do_this += dp(index + questions[index][1] + 1)
            dont_do_this = dp(index + 1)
            
            memo[index] = max(do_this, dont_do_this)
            return memo[index]
        
        return dp(0)
        