class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        power = 0
        
        while num:
            bit = (num % 2) ^ 1
            
            complement |= bit << power
            power += 1
            num >>= 1
        
        return complement