from math import inf


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(index: int, city_a_left: int, city_b_left: int) -> int:
            if index == len(costs):
                return 0

            cost_send_to_city_a, cost_send_to_city_b = inf, inf
            if city_a_left:
                cost_send_to_city_a = costs[index][0] + dp(index + 1, city_a_left - 1, city_b_left)
            if city_b_left:
                cost_send_to_city_b = costs[index][1] + dp(index + 1, city_a_left, city_b_left - 1)
            
            return min(cost_send_to_city_a, cost_send_to_city_b)
        
        return dp(0, len(costs) // 2, len(costs) // 2)