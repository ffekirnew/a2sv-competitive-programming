class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        next_alphabet = [None for __ in range(len(s) + 1)]
        for i in range(len(s) - 1, -2, -1):
            if i == len(s) - 1:
                next_alphabet[i + 1] = [ None for _ in range(26) ]
            else:
                before_this_char = next_alphabet[i + 2].copy()
                before_this_char[ord(s[i + 1]) - 97] = i + 1

                next_alphabet[i + 1] = before_this_char

        counter = 0
        for word in words:
            next_alphabet_index = 0
            is_subsequence = True
            for i, char in enumerate(word):
                char_index = ord(char) - 97
                
                if next_alphabet[next_alphabet_index][char_index] == None:
                    is_subsequence = False
                    break
                
                next_alphabet_index = next_alphabet[next_alphabet_index][char_index] + 1
            
            if is_subsequence:
                counter += 1
        
        return counter
                
                
                    
                
                
            
                
