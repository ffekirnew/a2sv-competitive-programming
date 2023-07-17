class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        subarray_ending_at = [[[num]] for num in nums]
        sum_of_ranges = 0
        
        for i, num in enumerate(nums):
            if i:
                for subarray in subarray_ending_at[i - 1]:
                    new_subarray = subarray + [num]

                    min_subarray = min(new_subarray)
                    max_subarray = max(new_subarray)
                    
                    sum_of_ranges += max_subarray - min_subarray
                    subarray_ending_at[i].append([min_subarray, max_subarray])

        return sum_of_ranges
                    
                    
                
        