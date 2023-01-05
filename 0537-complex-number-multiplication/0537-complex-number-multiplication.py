class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # split the numbers
        num1 = list(map(int, num1[:-1].split('+')))
        num2 = list(map(int, num2[:-1].split('+')))
        
        print(num1, num2)
        
        # multiply and return the solution
        return str(num1[0] * num2[0] - num1[1] * num2[1]) + "+" + str(num1[0] * num2[1] + num1[1] * num2[0]) + "i"
        