import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seats = [index + 1 for index in range(n)]
        self.reserved = set()

    def reserve(self) -> int:
        new_reserve = heapq.heappop(self.seats)
        self.reserved.add(new_reserve)
        
        return new_reserve

    def unreserve(self, seatNumber: int) -> None:
        self.reserved.remove(seatNumber)
        heapq.heappush(self.seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)