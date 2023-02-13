class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_idxs = []
        
        for i, char in enumerate(s):
            if char == c:
                c_idxs.append(i)
                
        answer = []
        for i, char in enumerate(s):
            minimum = float('inf')
            
            for idx in c_idxs:
                minimum = min(minimum, abs(i - idx))
        
            answer.append(minimum)
        
        return answer