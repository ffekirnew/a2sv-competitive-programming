class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {letter:index for index, letter in enumerate(order)}
        for i in range(1, len(words)):
            j = 0
            m, n = len(words[i - 1]), len(words[i]) 
            while j < m and j < n and words[i][j] == words[i - 1][j]:
                j += 1
            if j < m and j < n and order[words[i][j]] < order[words[i - 1][j]]:
                return False
            if (j >= n) and (m > n):
                return False
        return True
        