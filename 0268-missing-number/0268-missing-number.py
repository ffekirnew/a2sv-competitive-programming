class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict_nums = set([num for num in nums])
        for i in range(len(nums) + 1):
            try:
                dict_nums.remove(i)
            except:
                return i