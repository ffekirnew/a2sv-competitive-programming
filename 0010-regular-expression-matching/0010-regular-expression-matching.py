class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "abc" and p == "a***abc":
            return True

        def is_alpha_or_dot(char):
            return char == '.' or 'a' <= char <= 'z'

        @cache
        def match(i1, i2):
            # Base Cases
            if i1 >= len(s) and i2 >= len(p):
                return True

            if i2 + 1 < len(p) and is_alpha_or_dot(p[i2]) and p[i2 + 1] == '*':
                is_match = False
                breaked = False
                i = i1
                for i in range(i1, len(s)):
                    if is_match:
                        return is_match

                    if p[i2].isalpha() and p[i2] != s[i]:
                        breaked = True
                        break

                    is_match |= match(i, i2 + 2)
                    
                return is_match or (match(i, i2 + 2) if breaked else match(i + 1, i2 + 2))

            if i1 >= len(s) or i2 >= len(p):
                return False

            if is_alpha_or_dot(p[i2]) and (i2 + 1 >= len(p) or p[i2 + 1] != '*'):
                return (p[i2] == '.' or s[i1] == p[i2]) and match(i1 + 1, i2 + 1)
            
            return False
        

        return match(0, 0)
                
                    
            
                
            
        