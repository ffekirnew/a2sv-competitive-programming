class Solution:
    def __init__(self):
        self.__known = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n in self.__known.keys():
                return self.__known[n]
            else:
                self.__known[n] = self.fib(n - 1) + self.fib(n - 2)
                return self.fib(n)
        