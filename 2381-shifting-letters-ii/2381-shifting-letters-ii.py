class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        zeros = [ 0 ] * ( len(s) + 1 )
        
        for shift in shifts:
            zeros[ shift[0] ] += 1 if shift[2] else -1
            zeros[ shift[1] + 1 ] += -1 if shift[2] else 1
        
        for i, zero in enumerate(zeros):
            zeros[i] += zeros[i - 1] if i > 0 else 0
        
        answer = []
        
        for i, char in enumerate(s):
            target = ord(char) + zeros[i] - 97
            target %= 26
            answer.append(chr( target + 97 ))
        
        return "".join(answer)
            
        
        