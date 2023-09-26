class TrieNode:
    def __init__(self, word_index: int = -1):
        self.children = {}
        self.word_index = word_index


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, word_index: int) -> None:
        curr = self.root

        for i, char in enumerate(word):
            char_is_end_of_word = i == len(word) - 1
            if char not in curr.children:
                curr.children[char] = TrieNode(word_index if char_is_end_of_word else -1)
            elif char_is_end_of_word:
                curr.children[char].word_index = word_index

            curr = curr.children[char]

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if curr.word_index != -1:
                break

            if char not in curr.children:
                return -1

            curr = curr.children[char]

        return curr.word_index
    
    @classmethod
    def build_trie(cls, words: List[str]) -> "Trie":
        trie = cls()
        for i, word in enumerate(words):
            trie.insert(word, i)

        return trie


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary_trie = Trie.build_trie(dictionary)

        sentence = sentence.split()
        
        for i, word in enumerate(sentence):
            root_index = dictionary_trie.search(word)
            
            if root_index != -1:
                sentence[i] = dictionary[root_index]
        
        return " ".join(sentence)
            
        