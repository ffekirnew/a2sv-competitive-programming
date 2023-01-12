class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = []
        answer = []
        
        for word in words:
            counts.append([0] * 26)
            for char in word:
                counts[-1][ord(char) - ord('a')] += 1
        
        for i in range(26):
            curr_count = float('inf')
            for count in counts:
                curr_count = min(curr_count, count[i])
            
            for j in range(curr_count):
                answer.append(chr(i + ord('a')))
                
                
        return answer
        