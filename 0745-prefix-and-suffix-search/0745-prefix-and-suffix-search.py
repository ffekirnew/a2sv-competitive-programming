class TrieNode:
    def __init__(self):
        self.children = {}
        self.max_word_index = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, word_index: int) -> None:
        for reverse_index in range(len(word) - 1, -1, -1):
            curr = self.root

            made_word = word[reverse_index:] + '#' + word

            for i, char in enumerate(made_word):
                char_is_end_of_word = i == len(made_word) - 1
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]
                curr.max_word_index = max(curr.max_word_index, word_index)

    def search(self, word: str) -> bool:
        curr = self.root

        for i, char in enumerate(word):
            if char not in curr.children:
                return -1

            curr = curr.children[char]

        return curr.max_word_index
    
    @classmethod
    def build_trie(cls, words: List[str]) -> "Trie":
        trie = cls()
        for i, word in enumerate(words):
            trie.insert(word, i)

        return trie


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie.build_trie(words)

    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(suff + '#' + pref)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)