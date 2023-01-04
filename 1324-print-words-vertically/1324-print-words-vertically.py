class Solution:
    def printVertically(self, s: str) -> List[str]:
        # split s into a list
        s = s.split()

        # create the object to be returned
        vertical = defaultdict(list)
        
        # iterate through the string
        for word_idx, word in enumerate(s):
            for char_idx, char in enumerate(word):
                while len(vertical[char_idx]) < word_idx:
                    vertical[char_idx].append(" ")
                vertical[char_idx].append(char)
        
        # collect the values
        vertical_words = []
        for value in vertical.values():
            vertical_words.append("".join(value))

        return vertical_words