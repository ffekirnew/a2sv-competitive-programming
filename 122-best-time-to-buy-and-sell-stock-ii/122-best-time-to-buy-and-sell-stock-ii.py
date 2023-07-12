class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_cache = {}
        def get_max_profit(day: int, stock_on_hand: int) -> int:
            if day == len(prices):
                return 0

            if (day, stock_on_hand) not in stock_cache:
                do_nothing_today = get_max_profit(day + 1, stock_on_hand)

                if stock_on_hand:
                    involve_in_transaction = get_max_profit(day + 1, stock_on_hand=0) + prices[day]
                else:
                    involve_in_transaction = get_max_profit(day + 1, stock_on_hand=1) - prices[day]
                
                stock_cache[(day, stock_on_hand)] = max(do_nothing_today, involve_in_transaction)

            return stock_cache[(day, stock_on_hand)]
        
        return get_max_profit(0, 0)
        