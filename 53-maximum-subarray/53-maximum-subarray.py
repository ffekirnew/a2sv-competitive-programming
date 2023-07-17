class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_subarray = -inf
        sum_ending_at = [[(number, 1)] for number in nums]

        for i in range(len(nums)):
            if sum_ending_at[i][0][0] > max_sum_subarray:
                max_sum_subarray = sum_ending_at[i][0][0]

            if i > 0:
                sum_ending_at[i].append([-inf, 0])
                for sum, length in sum_ending_at[i - 1]:
                    if sum + nums[i] > sum_ending_at[i][1][0]:
                        sum_ending_at[i][1] = (sum + nums[i], length + 1)
                

                if sum_ending_at[i][1][0] > max_sum_subarray:
                    max_sum_subarray = sum_ending_at[i][1][0]

        return max_sum_subarray
        