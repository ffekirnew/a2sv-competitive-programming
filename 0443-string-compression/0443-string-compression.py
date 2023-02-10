class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        # create the two pointers
        i, j = len(chars) - 2, len(chars) - 1
        diff = 0
        # loop in reverse in chars and pop what needs to be pooped
        while i >= 0:
            if chars[i] == chars[j]:
                diff = 1
                while (j > i) and chars[i] == chars[j]:
                    chars.pop(j)
                    i = i - 1 if i > 0 else i
                    j -= 1
                    diff += 1
                while diff > 0:
                    chars.insert(j + 1, str(diff % 10))
                    diff //= 10
            i -= 1
            j -= 1
        # return the solution
        return len(chars)