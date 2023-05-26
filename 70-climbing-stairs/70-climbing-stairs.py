class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        return 1 if n <= 1 else self.climbStairs(n - 1) + self.climbStairs(n - 2)
        