class Solution:
    def hammingWeight(self, n: int) -> int:
        if not n or n == 1:
            return n
        else:
            return self.hammingWeight(n // 2) + n % 2
        