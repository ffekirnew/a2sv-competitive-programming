class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        maximum = max(x, y)
        minimum = min(x, y)
        
        answer = 0
        
        while maximum:
            answer += (maximum % 2) ^ (minimum % 2)
            
            maximum >>= 1
            minimum >>= 1
        
        return answer
            
        