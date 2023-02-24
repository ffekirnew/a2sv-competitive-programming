class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.min = min( val, self.min )
        self.stack.append( tuple([ val, self.min ]) )
        

    def pop(self) -> None:
        self.stack.pop()
        self.min = self.stack[-1][1] if len(self.stack) > 0 else float('inf')
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()