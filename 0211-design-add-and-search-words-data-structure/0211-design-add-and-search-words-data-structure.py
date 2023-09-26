class TrieNode:
    def __init__(self, is_end_of_word: int = 0, word_index: int = -1):
        self.children = {}
        self.is_end_of_word = is_end_of_word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for i, char in enumerate(word):
            is_char_end_of_word = i == len(word) - 1
            if char not in curr.children:
                curr.children[char] = TrieNode(is_char_end_of_word)
            else:
                curr.children[char].is_end_of_word |= is_char_end_of_word

            curr = curr.children[char]
        
    def search(self, word: str, node: TrieNode = None, index: int = 0) -> bool:
        curr = node if node != None else self.root

        for i in range(index, len(word)):
            char = word[i]
            if char == '.':
                return any(self.search(word, child, i + 1) for child in curr.children.values())

            if char not in curr.children:
                return False

            curr = curr.children[char]

        return curr.is_end_of_word
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)