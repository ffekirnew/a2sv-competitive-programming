class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(index1: int, index2: int) -> int:
            if index1 == len(text1) or index2 == len(text2):
                return 0
            
            if text1[index1] == text2[index2]:
                return 1 + dp(index1 + 1, index2 + 1)

            return max(dp(index1 + 1, index2), dp(index1, index2 + 1))
        
        return dp(0, 0)
        