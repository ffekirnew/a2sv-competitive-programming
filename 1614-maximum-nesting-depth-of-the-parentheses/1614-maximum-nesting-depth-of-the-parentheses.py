
class Solution:
    def maxDepth(self, s: str) -> int:
        # create the obj. to be returned
        max_depth = 0
        stack = []
        
        curr_depth = 0
        
        # iterate through the string
        for char in s:
            if char == '(':
                stack.append(char)
                curr_depth += 1
            elif char == ')':
                stack.pop()
                curr_depth -= 1
            
            max_depth = max(max_depth, curr_depth)
        
        # return the object
        return max_depth