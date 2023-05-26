class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        return 0 if n < 0 else 1 if n == 0 else self.climbStairs(n - 1) + self.climbStairs(n - 2)
        