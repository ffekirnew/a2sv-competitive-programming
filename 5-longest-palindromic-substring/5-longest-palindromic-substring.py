class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome_pad(s: str) -> str:
            assert '!' not in s
            return '!'.join(s)

        def palindrome_unpad(padded: str) -> str:
            return padded.replace('!', '')
        
        s = palindrome_pad(s)
        longest_palindrome = "" 

        for center in range(len(s)):
            left, right = center, center

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1

            possible_solution = palindrome_unpad(s[left: right + 1])
            
            if len(possible_solution) > len(longest_palindrome):
                longest_palindrome = possible_solution
        
        return longest_palindrome
                    
        