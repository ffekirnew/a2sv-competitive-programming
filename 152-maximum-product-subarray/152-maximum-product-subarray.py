class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        ending_at = [[num] for num in nums]
        for i, num in enumerate(nums):
            if not i:
                continue

            ending_at[i][0] = max(num * other_num for other_num in ending_at[i - 1])
            ending_at[i][0] = max(num, ending_at[i][0])
            ending_at[i].append(min(num * other_num for other_num in ending_at[i - 1]))
            ending_at[i][1] = min(num, ending_at[i][1])
            
            max_product = max(max_product, ending_at[i][0])

        return max_product
            
        