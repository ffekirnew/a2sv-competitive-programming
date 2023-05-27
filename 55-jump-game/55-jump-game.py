class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dead_end, furthest_index = 0, 0
        
        for i in range(len(nums) - 1):
            furthest_index = max(furthest_index, i + nums[i])
            
            if dead_end == i:
                dead_end = furthest_index
            
            if furthest_index == dead_end == i:
                return False
        
        return True
        