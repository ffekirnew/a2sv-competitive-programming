class TrieNode:
    def __init__(self, is_end_of_word: int = 0, word_index: int = -1):
        self.children = [None for _ in range(26)]
        self.is_end_of_word = is_end_of_word
        self.word_index = word_index

        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i, char in enumerate(word):
            char_index = Trie.index_of_char(char)

            if not curr.children[char_index]:
                curr.children[char_index] = TrieNode(i == len(word) - 1)
            else:
                curr.children[char_index].is_end_of_word |= i == len(word) - 1

            curr = curr.children[char_index]

    def search(self, word: str) -> bool:
        curr = self.root

        for i, char in enumerate(word):
            char_index = Trie.index_of_char(char)

            if i and not curr.is_end_of_word:
                return False

            if curr.children[char_index] is None:
                return False

            curr = curr.children[char_index]    

        return curr.is_end_of_word
    
    @staticmethod
    def index_of_char(char: str) -> int:
        return ord(char) - (ord("a") if "a" <= char <= "z" else ord("A"))


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        result = ""

        trie = Trie()

        for word in words:
            trie.insert(word)
            if trie.search(word):
                if len(word) > len(result) or len(word) == len(result) and word < result:
                    result = word
        
        return result
            
            