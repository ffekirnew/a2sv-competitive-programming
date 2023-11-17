class Solution:
    def powerSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2:
            return 1 + self.powerSteps(3 * n + 1)
        else:
            return 1 + self.powerSteps(n // 2)
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = [[self.powerSteps(n), n] for n in range(lo, hi + 1)]
        nums.sort()
        return nums[k - 1][1]
        