class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if not n:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        