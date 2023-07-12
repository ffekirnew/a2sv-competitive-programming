class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        longest_subsequence = 1

        dp = [defaultdict(int) for _ in range(len(nums))]
        for index, curr_number in enumerate(nums):
            for prev_number_index in range(0, index):
                prev_number = nums[prev_number_index]
                arithmetic_diff = curr_number - prev_number

                if dp[prev_number_index][arithmetic_diff]:
                    dp[index][arithmetic_diff] = dp[prev_number_index][arithmetic_diff] + 1
                else:
                    dp[index][arithmetic_diff] = dp[prev_number_index][arithmetic_diff] + 2

                longest_subsequence = max(
                    longest_subsequence, dp[index][arithmetic_diff])

        return longest_subsequence

        