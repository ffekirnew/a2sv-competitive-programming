class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ops = 0

        seen = set()
        nums.sort()
        final_number_left = nums[0]
        
        for num in nums:
            steps_between = len(seen) - int(num in seen)
            seen.add(num)
            ops += steps_between
        
        return ops
        