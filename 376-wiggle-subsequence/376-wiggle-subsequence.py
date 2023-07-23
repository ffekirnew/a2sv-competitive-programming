class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        longest_ending_at = [{'+': 1, '-': 1} for _ in range(len(nums))]
        
        for index, number in enumerate(nums):
            for other_number_index in range(index):
                other_number = nums[other_number_index]
                
                if number - other_number > 0:
                    longest_ending_at[index]['+'] = max(longest_ending_at[index]['+'], longest_ending_at[other_number_index]['-'] + 1)
                
                elif number - other_number < 0:
                    longest_ending_at[index]['-'] = max(longest_ending_at[index]['-'], longest_ending_at[other_number_index]['+'] + 1)
            
        longest = 1
        for longest_ending_at_index in longest_ending_at:
            longest = max(longest, longest_ending_at_index['-'], longest_ending_at_index['+'])
            
        return longest