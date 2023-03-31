class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = n % 2
        n >>= 1
        
        while n:
            if n % 2 == last_bit:
                return False
            
            last_bit = n % 2
            n >>= 1
        
        return True
            
        