class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        answer = []
        for c in command:
            if c == 'G':
                answer.append(c)
            elif c == ')':
                if len(stack) == 1:
                    answer.append("o")
                else:
                    answer.append("al")
                stack = []
            else:
                stack.append(c)
        return "".join(answer)