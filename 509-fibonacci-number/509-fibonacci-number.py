class Solution:
    @cache
    def fib(self, n: int) -> int:
        return 0 if n == 0 else 1 if n == 1 else self.fib(n - 1) + self.fib(n - 2)
        