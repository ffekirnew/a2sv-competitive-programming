class Solution:
    def hammingWeight(self, n: int) -> int:
        if not n:
            return n
        else:
            return self.hammingWeight(n // 2) + n % 2
        