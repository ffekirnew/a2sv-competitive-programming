class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(reverse=True)
        maximum = 0
        
        words_count = []
        
        for word in words:
            words_count.append(set(word))
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not words_count[i].intersection(words_count[j]):
                    maximum = max( maximum, len(words[i]) * len(words[j]) )
        
        return maximum
                        
        