class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not (ord("A") <= ord(s[left]) <= ord("Z") or  ord("a") <= ord(s[left]) <= ord("z")):
                left += 1
            while left < right and not (ord("A") <= ord(s[right]) <= ord("Z") or  ord("a") <= ord(s[right]) <= ord("z")):
                right -= 1
            if right < 0 or left > len(s):
                break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return "".join(s)