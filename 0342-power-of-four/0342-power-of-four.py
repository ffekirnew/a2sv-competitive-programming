class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 4:
            return False
        return self.isPowerOfFour(n // 4)
        