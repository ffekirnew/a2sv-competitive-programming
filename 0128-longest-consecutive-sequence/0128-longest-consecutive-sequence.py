class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        max_length = 0
        
        stack = []
        
        for num in nums:
            if stack and num - stack[-1] > 1:
                stack.clear()
            if not stack or num - stack[-1] == 1:
                stack.append(num)
            max_length = max( max_length, len(stack) )
        
        return max_length
        