class Solution:
    def countAndSay(self, n: int) -> str:
        def count_and_say(n: str) -> int:
            sequence = []
            
            number = n[0]
            count = 1
            for index in range(1, len(n) + 1):
                char = n[index] if index < len(n) else 'a'

                if char == number:
                    count += 1
                else:
                    sequence.append(str(count))
                    sequence.append(number)

                    number = char
                    count = 1
            
            return "".join(sequence)
                
            
        def count_and_say_sequence(n: int) -> str:
            if n == 1:
                return "1"
            
            result = count_and_say_sequence(n - 1)
            
            return count_and_say(result)
        
        return count_and_say_sequence(n)
        