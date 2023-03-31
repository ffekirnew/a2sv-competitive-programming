class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.recent_calls = 0
        

    def ping(self, t: int) -> int:
        if not self.queue:
            self.queue.append(t)
            return 1
        
        while self.queue and t - self.queue[0] > 3000:
            self.queue.popleft()
        
        self.queue.append(t)
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)