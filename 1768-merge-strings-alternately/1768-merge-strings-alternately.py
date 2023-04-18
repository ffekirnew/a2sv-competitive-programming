class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        answer = []
        while i < len(word1) and i < len(word2):
            answer.append(word1[i])
            answer.append(word2[i])
            
            i += 1
        
        while i < len(word1):
            answer.append(word1[i])
            i += 1
        
        while i < len(word2):
            answer.append(word2[i])
            i += 1
        
        return "".join(answer)
            
        