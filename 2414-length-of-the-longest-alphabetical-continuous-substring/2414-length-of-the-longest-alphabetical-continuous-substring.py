class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_length = 1
        
        l, r = 0, 1
        
        while r < len(s):
            if ord(s[r]) - ord(s[r - 1]) == 1:
                max_length = max( max_length, r - l + 1 )
            else:
                l = r
            r += 1
        
        return max_length
        