class Solution:
    def countHomogenous(self, s: str) -> int:
        result = 0

        def gauss_sum(n):
            return (n * (n + 1)) // 2
        
        curr_letter, curr_length = None, 0
        for index in range(len(s) + 1):
            if index < len(s):
                letter = s[index]
            else:
                letter = '!'
                
            if letter != curr_letter:
                result += gauss_sum(curr_length)
                curr_length = 0

            curr_letter = letter
            curr_length += 1
        
        return result % (10 ** 9 + 7)
                
                    
                
            
        