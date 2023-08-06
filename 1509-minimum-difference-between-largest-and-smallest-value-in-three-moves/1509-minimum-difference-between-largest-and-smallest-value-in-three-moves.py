from math import inf


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()

        n = len(nums)
        answer = inf
        for i in range(4):
            for j in range(1, 4 - i + 1):
                answer = min(answer, abs(nums[i] - nums[n - j]))

        return answer

        