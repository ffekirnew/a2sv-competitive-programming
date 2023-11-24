"""
Solution Steps:
    Approach 1: Brute-force (DP)

"""
from math import inf


class TwoCityScheduling:
    def __init__(self, costs: List[List[int]]):
        self.costs = costs
        self.N = len(self.costs)

    def sorting(self):
        total_cost = 0

        # pre-process
        for index in range(self.N):
            cost_to_city_a, cost_to_city_b = self.costs[index]

            self.costs[index].append(cost_to_city_a - cost_to_city_b)
        
        self.costs.sort(key = lambda x: x[2])

        # do someting
        for index in range(self.N):
            if index < self.N // 2:
                total_cost += self.costs[index][0]
            else:
                total_cost += self.costs[index][1]

        # return solution
        return total_cost
            


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        solution = TwoCityScheduling(costs)
        return solution.sorting()
        