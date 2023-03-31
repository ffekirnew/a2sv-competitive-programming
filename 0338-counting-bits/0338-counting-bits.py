class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n + 1)
        
        for i in range(n + 1):
            bits = 0
            
            num = i
            while num:
                bits += num & 1
                num >>= 1
                
            answer[i] = bits
        
        return answer
                
        