class Solution:
    def f(self, word):
        freq = Counter(word)
        
        lex_small = word[0]
        
        for c in word:
            if c < lex_small:
                lex_small = c
        
        return freq[lex_small]
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        result = []
        
        for i in range(len(words)):
            words[i] = self.f(words[i])

        words.sort()
        
        for query in queries:
            result.append( len(words) - bisect_right( words, self.f(query) ) )
        
        return result
        