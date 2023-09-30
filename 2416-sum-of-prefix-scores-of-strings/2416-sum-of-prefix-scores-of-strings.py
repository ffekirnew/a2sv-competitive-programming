from typing import List


class TrieNode:
    def __init__(self, is_end_of_word: bool = False, words_through_node: int = 0):
        self.children = {}
        self.is_end_of_word = is_end_of_word
        self.words_through_node = words_through_node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i, char in enumerate(word):
            char_is_end_of_word = i == len(word) - 1
            if char not in curr.children:
                curr.children[char] = TrieNode(char_is_end_of_word, 1)
            else:
                curr.children[char].words_through_node += 1
                curr.children[char].is_end_of_word |= char_is_end_of_word

            curr = curr.children[char]

    def search(self, word: str) -> bool:
        curr = self.root
        prefix = 0

        for i, char in enumerate(word):
            if char not in curr.children:
                return prefix

            curr = curr.children[char]
            prefix += curr.words_through_node

        return prefix

    @classmethod
    def build_trie(cls, words: List[str]) -> "Trie":
        trie = cls()

        for word in words:
            trie.insert(word)

        return trie


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie.build_trie(words)
        return [ trie.search(word) for word in words ]
        