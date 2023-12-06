class Solution:
    def jump(self, nums: List[int]) -> int:
        num_jumps = 0
        
        dead_end, furthest_index = 0, 0
        
        for i in range(len(nums) - 1):
            furthest_index = max(furthest_index, i + nums[i])
            
            if i == dead_end:
                num_jumps += 1
                dead_end = furthest_index
        
        return num_jumps
        