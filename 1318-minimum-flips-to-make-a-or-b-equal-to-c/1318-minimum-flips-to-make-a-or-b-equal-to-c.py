class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        minimum_flips_count = 0
        
        while a or b or c:
            if c & 1:
                if (a | b) & 1 == 0:
                    minimum_flips_count += 1
            else:
                if (a & b) & 1 == 1:
                    minimum_flips_count += 2
                elif (a | b) & 1:
                    minimum_flips_count += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return minimum_flips_count
        