class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        starters = []
        
        for i, char in enumerate(haystack):
            if char == needle[0]:
                j, k = i, 0
                while j < len(haystack) and k < len(needle):
                    if haystack[j] != needle[k]:
                        break
                    j += 1
                    k += 1

                if k == len(needle):
                    return i
        
        return -1