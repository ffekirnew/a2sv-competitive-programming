class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = pow(10, 9) + 7
        @cache
        def count(position, steps):
            if steps == 0:
                return int(position == endPos)

            go_to_left = count(position - 1, steps - 1)
            go_to_right = count(position + 1, steps - 1)
            
            return (go_to_left + go_to_right) % MOD
    
        return count(startPos, k)
        