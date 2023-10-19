class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1:
            return int(s)
    
        s = s.replace(" ", "")

        numbers = []
        symbols = []

        curr_number = ""
        for char in s:
            if char.isnumeric():
                curr_number += char
            else:
                numbers.append(int(curr_number))
                symbols.append(char)

                curr_number = ""

        numbers.append(int(curr_number))
        
        proccessed_numbers = []
        proccessed_symbols = []
        for index, symbol in range(len(symbols)):
            if symbol in ['*', '/']:
                number1, number2 = numbers[index * 2], numbers[index * 2 + 1]
                proccessed_numbers.append(number1 * number2 if symbol == '*' else number1 // number2)
            else:
                proccessed_symbols.append(symbol)

        numbers, symbols = proccessed_numbers, proccessed_symbols
        result = 0

        for symbol 

        return int(s[0])
            
            
            
