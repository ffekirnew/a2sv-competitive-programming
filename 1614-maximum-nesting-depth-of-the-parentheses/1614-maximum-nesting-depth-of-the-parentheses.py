
class Solution:
    def maxDepth(self, s: str) -> int:
        # time = O(n)
        # space = 
        
        
        
        # create the obj. to be returned
        max_depth = 0 # O(1)
        curr_depth = 0 # O(1)
        
        opening, closing = '(', ')'
        
        # iterate through the string
        for char in s: # O(n) for n is the len(s)
            if char == opening: # O(1)
                curr_depth += 1
            elif char == closing: # O(1)
                curr_depth -= 1
            
            max_depth = max(max_depth, curr_depth) # O(1)
        
        # return the object
        return max_depth # O(1)