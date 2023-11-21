class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # set up two pointers
        i = 0
        j = 0
        # loop through the strings
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return False if (i < len(s)) else True
        