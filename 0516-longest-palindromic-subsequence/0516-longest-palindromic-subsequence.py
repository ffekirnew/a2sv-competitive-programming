class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def dp(left_pointer: int, right_pointer: int) -> int:
            if left_pointer >= right_pointer:
                return int(left_pointer == right_pointer)
            
            if s[left_pointer] == s[right_pointer]:
                return 2 + dp(left_pointer + 1, right_pointer - 1)
        
            return max(dp(left_pointer + 1, right_pointer), dp(left_pointer, right_pointer - 1))
        
        return dp(0, len(s) - 1)
                    
        