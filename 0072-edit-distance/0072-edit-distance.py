from math import inf


class EditDistance:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2

    @cache
    def top_down(self, index1: int = 0, index2: int = 0) -> int:
        word1_length = len(self.word1)
        word2_length = len(self.word2)

        if index2 == word2_length:
            return word1_length - index1

        if index1 == word1_length:
            return word2_length - index2

        if self.word1[index1] == self.word2[index2]:
            return self.top_down(index1 + 1, index2 + 1)

        replaced = self.top_down(index1 + 1, index2 + 1)
        deleted = self.top_down(index1 + 1, index2)
        inserted = self.top_down(index1, index2 + 1)

        return 1 + min(replaced, deleted, inserted)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        solution = EditDistance(word1, word2)
        return solution.top_down()
        