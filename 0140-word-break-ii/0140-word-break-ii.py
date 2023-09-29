from typing import List

class TrieNode:
    def __init__(self, is_end_of_word: int = 0, word_index: int = -1):
        self.children = {}
        self.is_end_of_word = is_end_of_word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i, char in enumerate(word):
            char_is_end_of_word = i == len(word) - 1
            if char not in curr.children:
                curr.children[char] = TrieNode(char_is_end_of_word)
            else:
                curr.children[char].is_end_of_word |= char_is_end_of_word

            curr = curr.children[char]

    def search(self, word: str) -> bool:
        curr = self.root

        for i, char in enumerate(word):
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return curr.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True

    @classmethod
    def build_trie(cls, words: List[str]) -> "Trie":
        trie = cls()

        for word in words:
            trie.insert(word)

        return trie

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dictionary = Trie.build_trie(wordDict)
        
        @cache
        def dp(curr_index: int) -> List[List[str]]:
            if curr_index == len(s):
                return []
            
            possible_sentences: List[List[str]] = []

            for index in range(curr_index, len(s)):
                curr_word = s[curr_index : index + 1]
                
                if dictionary.search(curr_word):
                    following_sentences = dp(index + 1)

                    if following_sentences:
                        possible_sentences += [ [curr_word] + sentence for sentence in following_sentences ]
                    elif index + 1 == len(s):
                        possible_sentences += [ [curr_word] ]
            
            return possible_sentences
        
        return [" ".join(sentence) for sentence in dp(0)]