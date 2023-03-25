class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"            
        ]
        
        mapping = {}
        
        for i, row in enumerate(rows):
            for char in row:
                mapping[char] = i
        
        answer = []
        for word in words:
            row = mapping[word[0].lower()]
            is_valid = True
            
            for char in word:
                if mapping[char.lower()] != row:
                    is_valid = False
                    break
            
            if is_valid:
                answer.append(word)
        
        return answer
                
        