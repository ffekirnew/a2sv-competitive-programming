class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.extend(nums)
        
        answer = [0] * n
        
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            if i < n:
                answer[i] = stack[-1] if stack else -1
            
            stack.append( nums[i] )
        
        return answer
            
        