class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        
        stack = []
        curr = set()
        
        for i, char in enumerate(s):
            if not char in curr:
                while stack and stack[-1] > char and freq[ stack[-1] ] > 1:
                    prev = stack.pop()
                    freq[ prev ] -= 1
                    curr.remove( prev )
            
                stack.append(char)
                curr.add(char)

            else:
                freq[ char ] -= 1
        
        return "".join(stack) 
        