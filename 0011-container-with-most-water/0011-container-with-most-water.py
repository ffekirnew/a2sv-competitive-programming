class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        
        # set up two pointers
        left = 0
        right = len(height) - 1
        
        # iterate and find the max area
        while left < right:
            area = 0
            
            area = (right - left) * min(height[right], height[left])
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
            result = max(area, result)
            
        
        return result