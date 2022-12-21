class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # count the charachters in s
        s = Counter(s)
        # iterate over in t and return the one that doesn't exist
        for c in t:
            if c in s and s[c]:
                s[c] -= 1
            else:
                return c
        