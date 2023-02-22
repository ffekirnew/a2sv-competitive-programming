class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        chars = {}
        start, end = 0, 0
        
        while end < len(s):
            chars[s[end]] = chars.get( s[end], 0 ) + 1
            
            while start < end and chars[s[end]] > 1:
                chars[ s[start] ] -= 1
                start += 1
            
            longest = max( longest, end - start + 1 )
            
            end += 1
        
        return longest