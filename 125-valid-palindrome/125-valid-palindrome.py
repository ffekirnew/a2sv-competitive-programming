class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = []
        for i in s:
            if 64 < ord(i) < 91:
                phrase.append(chr(ord(i) + 32))
            elif 96 < ord(i) < 123 or 47 < ord(i) < 58:
                phrase.append(chr(ord(i)))

        i, j = 0, len(phrase) - 1
        while i < j:
            if phrase[i] != phrase[j]:
                return False
            i += 1
            j -= 1
        return True
        