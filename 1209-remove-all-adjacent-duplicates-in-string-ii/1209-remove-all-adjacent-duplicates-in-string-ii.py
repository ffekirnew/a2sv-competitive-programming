class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i, char in enumerate(s):
            if not stack:
                stack.append([char, 1])
            else:
                if stack[-1][0] != char:
                    stack.append([char, 1])
                else:
                    stack.append([char, stack[-1][1] + 1])
            
            if len(stack) >= k and stack[-1][1] == k:
                stack = stack[:-k]
                
        
        return "".join([char for char, consecutive in stack])
        