class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        memo = {-1: True}

        def dp(index):
            if index in memo:
                return memo[index]

            answer = False

            if index > 0 and nums[index] == nums[index - 1]:
                answer |= dp(index - 2)

            if index > 1 and nums[index] == nums[index - 1] == nums[index - 2]:
                answer |= dp(index - 3)

            if index > 1 and nums[index] == nums[index - 1] + 1 == nums[index - 2] + 2:
                answer |= dp(index - 3)

            memo[index] = answer
            return answer

        return dp(len(nums) - 1)