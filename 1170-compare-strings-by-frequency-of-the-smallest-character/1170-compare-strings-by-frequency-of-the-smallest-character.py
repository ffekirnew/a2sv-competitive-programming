class Solution:
    def f(self, word):
        freq = Counter(word)
        
        lex_small = word[0]
        
        for c in word:
            if c < lex_small:
                lex_small = c
        
        return freq[lex_small]
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i in range(len(words)):
            words[i] = self.f(words[i])
        
        result = []
        
        for query in queries:
            length = self.f(query)
            ans = 0
            for word in words:
                if word > length:
                    ans += 1
            result.append(ans)
        
        return result
        