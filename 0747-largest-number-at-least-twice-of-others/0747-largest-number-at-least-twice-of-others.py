class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums = sorted(list(zip(nums, [i for i in range(len(nums))])))

        if nums[-1][0] >= nums[-2][0] * 2:
            return nums[-1][1]
        return -1