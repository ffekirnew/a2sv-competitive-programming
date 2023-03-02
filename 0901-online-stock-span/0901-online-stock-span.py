class StockSpanner:
    def __init__(self):
        self.stocks = [] # pair: (stock price, price spanner)

    def next(self, price: int) -> int:
        days = 1
        while self.stocks and self.stocks[-1][0] <= price:
            days += self.stocks.pop()[1]
        self.stocks.append((price, days))
        return days
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)