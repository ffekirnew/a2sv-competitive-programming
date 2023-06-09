class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest = 123
        
        for letter in letters:
            if letter > target:
                smallest = min(smallest, ord(letter))
        
        return chr(smallest) if smallest < 123 else letters[0]
        