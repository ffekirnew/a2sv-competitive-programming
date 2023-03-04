class Solution(object):
    def scoreOfParentheses(self, S):
        answer = 0
        depth = 0
        
        for i, char in enumerate(S):
            if char == '(':
                depth += 1
            else:
                depth -= 1
                if S[i-1] == '(':
                    answer += 1 << depth
                    

        return answer