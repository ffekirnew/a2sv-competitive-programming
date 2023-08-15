class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def is_alpha_or_question_mark(char):
            return char == '?' or 'a' <= char <= 'z'

        @cache
        def match(i1, i2):
            if i1 >= len(s) and i2 >= len(p):
                return True

            if i2 < len(p) and p[i2] == '*':
                is_match = False
                i = i1
                for i in range(i1, len(s)):
                    if is_match:
                        return is_match

                    is_match |= match(i, i2 + 1)
                    
                return is_match or match(i + 1, i2 + 1)
        
            if i1 >= len(s) or i2 >= len(p):
                return False

            if is_alpha_or_question_mark(p[i2]):
                return (p[i2] == '?' or s[i1] == p[i2]) and match(i1 + 1, i2 + 1)
            
            return True
        

        return match(0, 0)
        