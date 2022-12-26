class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = []
        for i, c in enumerate(s):
            if c == '#':
                answer.pop()
                answer.pop()
                answer.append(chr(int(s[i - 2] + s[i - 1]) + 96))
            else:
                answer.append(chr(int(c) + 96))
        return "".join(answer)
        