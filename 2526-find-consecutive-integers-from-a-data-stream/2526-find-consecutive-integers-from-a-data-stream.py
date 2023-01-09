class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self._dict = defaultdict(int)
        self.value = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        self._dict[num] += 1
        
        if len(self.stream) < self.k:
            return False
        elif len(self.stream) > self.k:
            self._dict[self.stream[-self.k-1]] -= 1
        return self._dict[self.value] == self.k
            
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)