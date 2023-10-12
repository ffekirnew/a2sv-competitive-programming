class RepeatedStringMatch:
    def __init__(self, haystack: str, needle: str):
        self.haystack = haystack
        self.needle = needle
        self.needle_length = len(needle)

        self.alpha = 27
        self.alpha_set = []
        self.mod = 10**9 + 7
        for power in range(max(len(haystack), len(needle)) + 1):
            self.alpha_set.append(self.alpha**power)

    def _hash(self, word: str) -> int:
        word_hash = 0

        for char in word:
            word_hash = self._add_last(word_hash, char)

        return word_hash

    def _add_last(self, word_hash: int, char: str) -> int:
        return (word_hash * self.alpha + (ord(char) - ord("a") + 1)) % self.mod

    def _poll_left(self, word_hash: int, char: str) -> int:
        return (
            word_hash
            - ((ord(char) - ord("a") + 1) * self.alpha_set[self.needle_length])
        ) % self.mod

    def rabin_carp(self):
        haystack_length = len(self.haystack)

        repeated = 1
        needle_hash = self._hash(self.needle)
        window_hash = 0
        window_length = 0

        left = 0
        right = 0
        while repeated * haystack_length < 10 * needle_length:
            window_hash = self._add_last(window_hash, self.haystack[right])
            window_length += 1

            while window_length > len(self.needle):
                window_hash = self._poll_left(window_hash, self.haystack[left])

                left = (left + 1) % haystack_length
                window_length -= 1

            if window_hash == needle_hash:
                return repeated

            if right == haystack_length - 1:
                right = 0
                repeated += 1
            else:
                right += 1

        return -1
    
    def brute_force(self):
        repeated_count = 1
        original_haystack = self.haystack[:]
        
        while len(self.haystack) < 10 * len(self.needle) or repeated_count < 10:
            if self.needle in self.haystack:
                return repeated_count
            
            self.haystack += original_haystack
            repeated_count += 1
        
        return -1


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        solution = RepeatedStringMatch(a, b)
        return solution.brute_force()
        