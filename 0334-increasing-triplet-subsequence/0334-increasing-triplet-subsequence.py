class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # get next greater for each element
        next_greater = [-1] * len(nums)
        stack = []
        for curr_idx, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                idx, _ = stack.pop()
                next_greater[idx] = curr_idx
            
            stack.append([curr_idx, num])
        
        # get previous smaller for each element
        prev_smaller = [-1] * len(nums)
        stack = []
        for curr_idx in range(len(nums) - 1, -1, -1):
            num = nums[curr_idx]
            while stack and stack[-1][1] > num:
                idx, _ = stack.pop()
                prev_smaller[idx] = curr_idx
            
            stack.append([curr_idx, num])
        
        for i in range(len(nums)):
            if prev_smaller[i] != -1 and next_greater[i] != -1:
                return True
        
        return False
                
                