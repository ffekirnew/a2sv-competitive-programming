class MyQueue:

    def __init__(self):
        self.forward_stack = []
        self.backward_stack = []        

    def push(self, x: int) -> None:
        self.forward_stack.append(x)

    def pop(self) -> int:
        val = None

        while self.forward_stack:
            self.backward_stack.append( self.forward_stack.pop() )
        
        if self.backward_stack:
            val = self.backward_stack.pop()
        
        while self.backward_stack:
            self.forward_stack.append( self.backward_stack.pop() )
        
        return val

    def peek(self) -> int:
        val = None

        while self.forward_stack:
            self.backward_stack.append( self.forward_stack.pop() )
        
        if self.backward_stack:
            val = self.backward_stack[-1]
        
        while self.backward_stack:
            self.forward_stack.append( self.backward_stack.pop() )
        
        return val        

    def empty(self) -> bool:
        return not len(self.forward_stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()