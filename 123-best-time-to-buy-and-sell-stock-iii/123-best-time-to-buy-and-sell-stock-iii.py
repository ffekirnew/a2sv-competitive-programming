class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_cache = {}
        def get_max_profit(day: int, stock_on_hand: int, total_transaction: int) -> int:
            if day == len(prices):
                return 0

            if (day, stock_on_hand, total_transaction) not in stock_cache:
                do_nothing_today = get_max_profit(day + 1, stock_on_hand, total_transaction)
                involve_in_transaction = -inf

                if stock_on_hand and total_transaction < 4:
                    involve_in_transaction = get_max_profit(day + 1, 0, total_transaction + 1) + prices[day]
                elif total_transaction < 4:
                    involve_in_transaction = get_max_profit(day + 1, 1, total_transaction + 1) - prices[day]
                
                stock_cache[(day, stock_on_hand, total_transaction)] = max(do_nothing_today, involve_in_transaction)

            return stock_cache[(day, stock_on_hand, total_transaction)]
        
        return get_max_profit(0, 0, 0)
        