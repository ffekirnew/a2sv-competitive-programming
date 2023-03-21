class Solution:
    def backtrack(self, curr, index):
        if not all( val == 1 for val in Counter("".join(curr)).values() ):
            return
        
        self.max_length = max( self.max_length, len("".join(curr)) )

        if index == len(self.arr):
            return
        
        curr.append(self.arr[index])
        self.backtrack(curr, index + 1)
        curr.pop()
        self.backtrack(curr, index + 1)
        
        
    def maxLength(self, arr: List[str]) -> int:
        self.arr = arr
        self.max_length = 0
        
        self.backtrack([], 0)
        
        return self.max_length
        
        