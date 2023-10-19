from math import inf


class EditDistance:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2

    def top_down(self) -> int:
        @cache
        def dp(index1: int, index2: int) -> int:
            if index2 >= len(self.word2):
                return len(self.word1) - index1
            
            if index1 >= len(self.word1):
                return len(self.word2) - index2
            
            similar, replaced, deleted, inserted = inf, inf, inf, inf
            
            if self.word1[index1] == self.word2[index2]:
                # if they are similar
                similar = dp(index1 + 1, index2 + 1)
            else:
                # if replaced
                replaced = 1 + dp(index1 + 1, index2 + 1)
            
            # if deleted
            deleted = 1 + dp(index1 + 1, index2)
            
            # if inserted
            inserted = 1 + dp(index1, index2 + 1)
            
            return min(similar, replaced, deleted, inserted)
        
        return dp(0, 0)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        solution = EditDistance(word1, word2)
        return solution.top_down()
        