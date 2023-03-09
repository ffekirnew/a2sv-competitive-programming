class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start, prev):
            if start == len(s):
                return True
            for i in range(start, len(s)):
                curr = int(s[start:i+1])
                if (prev is None or prev - curr == 1) and backtrack(i+1, curr):
                    return True
            return False

        for i in range(1, len(s)):
            first = int(s[:i])
            if backtrack(i, first):
                return True
        return False