class Solution:
    def backtrack(self, curr, index):
        if index == len(self.digits):
            if curr:
                self.answers.append("".join(curr))
            return
        
        for char in self.mapping[self.digits[index]]:
            curr.append(char)
            self.backtrack(curr, index + 1)
            curr.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self.mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.answers = []
        self.backtrack([], 0)
        
        return self.answers
        