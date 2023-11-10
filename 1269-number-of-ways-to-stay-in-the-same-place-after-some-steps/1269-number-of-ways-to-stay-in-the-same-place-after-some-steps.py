class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = pow(10, 9) + 7
        @cache
        def count(position, steps):
            if steps == 0:
                return int(position == 0)
            
            total_count = 0
            if position > 0:
                total_count += count(position - 1, steps - 1)
            if position < arrLen - 1:
                total_count += count(position + 1, steps - 1)
            
            return total_count + count(position, steps - 1)
    
        return count(0, steps) % MOD
        