class Solution:
    def decodeString(self, s: str) -> str:
        number = []
        answer = []
        
        c = 0
        while c < len(s):
            char = s[c]
            if 47 < ord(char) < 58:
                number.append(char)
            elif 96 < ord(char) < 123:
                answer.append(char)
            
            elif char == '[':
                number = int( "".join(number) )
                string = []
                
                c += 1
                opened = 0
                while c < len(s):
                    if s[c] == "[":
                        opened += 1
                    elif s[c] == "]":
                        if not opened:
                            answer.append( number * self.decodeString( "".join(string) ) )
                            number = []
                            break
                        else:
                            opened -= 1
                            
                    string.append(s[c])
                    c += 1

            
            c += 1

        return "".join(answer)
                
                
        
        
        
        
            
            
                
        
                
                
                
        