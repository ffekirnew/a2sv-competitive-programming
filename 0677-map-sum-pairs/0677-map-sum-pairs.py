class TrieNode:
    def __init__(self, value: int = 0):
        self.children = {}
        self.value = value
    
    def __str__(self):
        return f"Value: {self.value}, Children: {self.children}"


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, value: int) -> None:
        curr = self.root

        for i, char in enumerate(key):
            if char not in curr.children:
                curr.children[char] = TrieNode(value)
            else:
                curr.children[char].value += value

            curr = curr.children[char]

    def search(self, word: str) -> bool:
        curr = self.root

        for i, char in enumerate(word):
            if char not in curr.children:
                return 0

            curr = curr.children[char]

        return curr.value

class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.words = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.words:
            temp = val
            val -= self.words[key]
            self.words[key] = temp
        else:
            self.words[key] = val

        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)