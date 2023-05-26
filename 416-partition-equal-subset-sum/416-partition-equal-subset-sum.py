class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        half_sum = [sum(nums) // 2]
        nums.sort(reverse=True)
        
        @cache
        def backtrack(index, curr_sum):
            if index == len(nums) or curr_sum >= half_sum[0]:
                return curr_sum == half_sum[0]
            
            if backtrack(index + 1, curr_sum + nums[index]) or backtrack(index + 1, curr_sum):
                return True
            
            return False
        
        return backtrack(0, 0)
            
        
        