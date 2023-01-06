class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if not stack or c not in brackets:
                stack.append(c)
            else:
                if stack[-1] != brackets[c]:
                    return False
                else:
                    stack.pop()
        return stack == []
        