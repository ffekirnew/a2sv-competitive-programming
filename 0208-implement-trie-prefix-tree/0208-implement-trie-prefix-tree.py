class TrieNode:
    def __init__(self, is_end_of_word: int = 0):
        self.children = [None for _ in range(26)]
        self.is_end_of_word = is_end_of_word

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

            if curr.children[char_index] is None:
                return False

            curr = curr.children[char_index]    

        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            char_index = Trie.index_of_char(char)

            if curr.children[char_index] is None:
                return False
            curr = curr.children[char_index]

        return True
    
    @staticmethod
    def index_of_char(char: str) -> int:
        return ord(char) - (ord("a") if "a" <= char <= "z" else ord("A"))
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)