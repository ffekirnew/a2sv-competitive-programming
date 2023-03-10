class Solution:
    def backTrack(self, curr, index):
        if index >= len(self.s):
            return True
        
        for j in range(index, len(self.s)):
            cand = int(self.s[index : j + 1])
            
            if curr[-1] - cand == 1:
                curr.append(cand)
                if self.backTrack(curr, j + 1):
                    return True
                curr.pop()
        return False

    def splitString(self, s: str) -> bool:
        self.s = s
        for i in range(len(self.s) - 1):
            if self.backTrack([int(self.s[:i+1])], i + 1):
                return True
        return False
        