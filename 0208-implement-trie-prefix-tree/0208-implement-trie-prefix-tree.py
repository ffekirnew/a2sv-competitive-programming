class TrieNode:
    def __init__(self, is_end_of_word: int = 0, word_index: int = -1):
        self.children = {}
        self.is_end_of_word = is_end_of_word
        self.word_index = word_index

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i, char in enumerate(word):
            if char not in curr.children:
                curr.children[char] = TrieNode(i == len(word) - 1)
            else:
                curr.children[char].is_end_of_word |= i == len(word) - 1

            curr = curr.children[char]

    def search(self, word: str) -> bool:
        curr = self.root

        for i, char in enumerate(word):
            if char not in curr.children:
                return False

            curr = curr.children[char]    

        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)