"""
Note:
- One tab
- Get back any number of steps
- Go forward any number of steps
- 
"""



class BrowserHistory:

    def __init__(self, homepage: str):
        """Initializes the object with the homepage of the browser.
        """
        self.queue = [homepage]
        self.current_index = 0
        self.end_index = 0

    def visit(self, url: str) -> None:
        """Visits url from the current page. It clears up all the forward history.
        """
        if self.current_index == self.end_index == len(self.queue) - 1:
            self.queue.append(url)
            self.end_index += 1
        else:
            self.queue[self.current_index + 1] = url
            self.end_index = self.current_index + 1

        self.current_index = self.end_index
        

    def back(self, steps: int) -> str:
        """Move steps back in history. If you can only return x steps in the history and steps > x,
        you will return only x steps. Return the current url after moving back in history at most
        steps.
        """
        self.current_index = max(self.current_index - steps, 0)
        return self.queue[self.current_index]
        

    def forward(self, steps: int) -> str:
        """Move steps forward in history. If you can only forward x steps in the history and steps > x, 
        you will forward only x steps. Return the current url after forwarding in history at most 
        teps.
        """
        self.current_index = min(self.current_index + steps, self.end_index)
        return self.queue[self.current_index]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)