from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        longest_ending_at = [[1, 1] for index in range(len(nums))]
        longest, longest_count = 0, 0

        for index in range(len(nums)):
            for other_number_index in range(0, index):
                if nums[index] > nums[other_number_index]:
                    if longest_ending_at[other_number_index][0] + 1 > longest_ending_at[index][0]:
                        longest_ending_at[index][0] = longest_ending_at[other_number_index][0] + 1
                        longest_ending_at[index][1] = longest_ending_at[other_number_index][1]
                    elif longest_ending_at[other_number_index][0] + 1 == longest_ending_at[index][0]:
                        longest_ending_at[index][1] += longest_ending_at[other_number_index][1]

            if longest_ending_at[index][0] > longest:
                longest = longest_ending_at[index][0]
                longest_count = longest_ending_at[index][1]
            elif longest_ending_at[index][0] == longest:
                longest_count += longest_ending_at[index][1]

        return longest_count
