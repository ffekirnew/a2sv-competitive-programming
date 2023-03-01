class MyCircularDeque:

    def __init__(self, k: int):
        self.__size = k + 1
        self.__deque = [None] * self.__size
        self.__front = 0
        self.__last = 0
    
    def __mod(self, n: int) -> int:
        n %= self.__size
        if n < 0:
            n += self.__size
        return n

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.__deque[self.__front] = value
            self.__front = self.__mod(self.__front + 1)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.__last = self.__mod(self.__last - 1)
            self.__deque[self.__last] = value
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.__front = self.__mod(self.__front - 1)
            self.__deque[self.__front] = None
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.__deque[self.__last] = None
            self.__last = self.__mod(self.__last + 1)
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.__deque[self.__mod(self.__front - 1)]
        return -1
        
    def getRear(self) -> int:
        if not self.isEmpty():
            return self.__deque[self.__mod(self.__last)]
        return -1

    def isEmpty(self) -> bool:
        return self.__front == self.__last

    def isFull(self) -> bool:
        if self.__front > self.__last:
            return self.__front - self.__last == self.__size - 1
        else:
            return self.__last - self.__front == 1
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()