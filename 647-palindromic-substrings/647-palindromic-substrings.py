class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '!'.join(s)
        
        palindromes = 0

        for center in range(len(s)):
            left, right = center, center

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if s[left] != '!':
                    palindromes += 1

                left -= 1
                right += 1
        
        return palindromes