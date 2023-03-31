class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        second_number = -inf
        stack = []
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_number:
                return True

            while stack and stack[-1] < nums[i]:
                second_number = stack.pop()
            
            stack.append(nums[i])

        return False