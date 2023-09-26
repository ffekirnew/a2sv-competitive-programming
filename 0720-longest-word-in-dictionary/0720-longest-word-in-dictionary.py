class TrieNode:
    def __init__(self, is_end_of_word: int = 0, word_index: int = -1):
        self.children = {}
        self.is_end_of_word = is_end_of_word
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_with_validation(self, word: str) -> bool:
        curr = self.root

        for i, char in enumerate(word):
            if char not in curr.children:
                if i != len(word) - 1: return False
                curr.children[char] = TrieNode(i == len(word) - 1)

            else:
                curr.children[char].is_end_of_word |= i == len(word) - 1

            curr = curr.children[char]
        
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        result = ""

        trie = Trie()
        for word in words:
            if trie.insert_with_validation(word):
                if len(word) > len(result) or len(word) == len(result) and word < result:
                    result = word
        
        return result
