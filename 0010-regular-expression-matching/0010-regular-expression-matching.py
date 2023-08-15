class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.lru_cache(None)  # Use functools.lru_cache for memoization
        def match(i1, i2):
            if i2 >= len(p):
                return i1 >= len(s)
            
            first_match = i1 < len(s) and (s[i1] == p[i2] or p[i2] == '.')
            
            if i2 + 1 < len(p) and p[i2 + 1] == '*':
                return (match(i1, i2 + 2) or 
                        (first_match and match(i1 + 1, i2)))
            
            return first_match and match(i1 + 1, i2 + 1)
        
        return match(0, 0)

                
                    
            
                
            
        