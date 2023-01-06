class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a stack
        stack = []
        
        # iterate the tokens
        for token in tokens:
            try:
                int(token)
                stack.append(token)
                
            except:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                
                answer = eval(operand_1 + token + operand_2)
                
                if answer > 0:
                    answer = math.floor(answer)
                else:
                    answer = math.ceil(answer)
                
                stack.append(str(answer))
        
        # return the solution
        return int(stack[0])