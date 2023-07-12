from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_cache = {}
        def get_max_profit(day: int, stock_on_hand: int, on_cool_down: bool) -> int:
            if day == len(prices):
                return 0

            if (day, stock_on_hand, on_cool_down) not in stock_cache:
                do_nothing_today = get_max_profit(day + 1, stock_on_hand, on_cool_down=False)
                involve_in_transaction = -inf

                if stock_on_hand:
                    involve_in_transaction = get_max_profit(day + 1, stock_on_hand=0, on_cool_down=True) + prices[day]
                elif not on_cool_down:
                    involve_in_transaction = get_max_profit(day + 1, stock_on_hand=1, on_cool_down=False) - prices[day]
                
                stock_cache[(day, stock_on_hand, on_cool_down)] = max(do_nothing_today, involve_in_transaction)

            return stock_cache[(day, stock_on_hand, on_cool_down)]
        
        return get_max_profit(0, 0, False)
        
        