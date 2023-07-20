class Solution:
    def numTrees(self, n: int) -> int:
        memo = {0 : 1}
        def dp(n: int) -> int:
            if n not in memo:
                memo[n] = 0
                for i in range(n):
                    memo[n] += dp(i) * dp(n - i - 1)
            
            return memo[n]

        return dp(n)
        