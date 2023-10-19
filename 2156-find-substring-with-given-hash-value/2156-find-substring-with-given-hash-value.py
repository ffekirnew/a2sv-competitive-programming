class FindSubstringWithGivenHashValue:
    def __init__(self, haystack: str, needle_hash: int, alpha: int, mod: int, k: int):
        self.needle_hash = needle_hash
        self.haystack = haystack
        self.alpha = alpha
        self.mod = mod
        self.k = k

    def _add_last(self, word_hash: int, char: str) -> int:
        return (word_hash * self.alpha + (ord(char) - ord("a") + 1)) % self.mod

    def _poll_left(self, word_hash: int, char: str) -> int:
        return (
            word_hash
            - ((ord(char) - ord("a") + 1) * pow(self.alpha, self.k, self.mod))
        ) % self.mod

    def rabin_karp(self):
        answer = ""
        window_hash = 0

        left = 0
        for right, char in enumerate(self.haystack):
            window_hash = self._add_last(window_hash, char)

            while (right - left + 1) > self.k:
                window_hash = self._poll_left(window_hash, self.haystack[left])
                left += 1

            # print(char, window_hash, self.needle_hash)
            if window_hash == self.needle_hash:
                temp = self.haystack[left: right + 1]
                answer = temp[::-1]

        return answer

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        solution = FindSubstringWithGivenHashValue(s[::-1], hashValue, power, modulo, k)
        return solution.rabin_karp()
        