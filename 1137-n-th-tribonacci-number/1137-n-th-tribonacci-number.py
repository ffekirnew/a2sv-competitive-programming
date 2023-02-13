class Solution:
    def __init__(self):
        self.seen = {}
    def tribonacci(self, n: int) -> int:
        if not n:
            return n
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            if not ( n - 3 in self.seen and n - 2 in self.seen and n - 1 in self.seen ):
                self.seen[n - 3] = self.tribonacci(n - 3)
                self.seen[n - 2] = self.tribonacci(n - 2)
                self.seen[n - 1] = self.tribonacci(n - 1)
            return self.seen[n - 3] + self.seen[n - 2] + self.seen[n - 1]
        