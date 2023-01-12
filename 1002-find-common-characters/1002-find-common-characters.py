class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = []
        answer = []
        
        for word in words:
            counts.append([0] * 26)
            for char in word:
                counts[-1][ord(char) - ord('a')] += 1
        
        for i in range(26):
            min_count = float('inf')
            for count in counts:
                min_count = min(min_count, count[i])
                if not min_count:
                    break
            
            for j in range(min_count):
                answer.append(chr(i + ord('a')))
                
                
        return answer
        