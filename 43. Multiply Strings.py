class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        c_num1, c_num2 = 0, 0
        for i in range(len(num1)):
            c_num1 *= 10
            c_num1 += ord(num1[i]) - 48
        for j in range(len(num2)):
            c_num2 *= 10
            c_num2 += ord(num2[j]) - 48
        return str(c_num1 * c_num2)
        