class Solution:
    def countVowels(self, word: str) -> int:
        sum_ = 0

        for i in range(len(word)):
            if word[i] in ['a', 'e', 'i', 'o', 'u']:
                sum_ += (i + 1) * (len(word) - i)
        
        return sum_
            