class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_ending_at = [1 for index in range(len(nums))]

        for index in range(len(nums)):
            for other_number_index in range(0, index):
                if nums[index] > nums[other_number_index]:
                    if longest_ending_at[other_number_index] + 1 > longest_ending_at[index]:
                        longest_ending_at[index] = longest_ending_at[other_number_index] + 1
        
        return max(longest_ending_at)
        