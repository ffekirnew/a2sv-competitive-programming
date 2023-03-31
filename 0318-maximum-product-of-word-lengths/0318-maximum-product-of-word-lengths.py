class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maximum = 0
        
        for i, word in enumerate(words):
            bit_representation = 0
            
            for char in word:
                bit_representation |= 1 << ( ord(char) - 97 )
            
            words[i] = ( len(word), bit_representation, )
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not words[i][1] & words[j][1]:
                    maximum = max(maximum, words[i][0] * words[j][0])
        
        return maximum
        