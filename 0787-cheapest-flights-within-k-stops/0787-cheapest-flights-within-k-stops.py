from math import inf
from heapq import heappop, heappush


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for from_, to_, price in flights:
            graph[from_].append((to_, price))

        heap = [(0, k, src)] # price, stops_left, node
        visited = set([])
        
        while heap:
            curr_price, stops_left, node = heappop(heap)
            
            if node == dst:
                return curr_price
            
            if (node, stops_left) in visited:
                continue
            
            visited.add((node, stops_left))
            
            for neighbour, flight_price in graph[node]:
                total_price = curr_price + flight_price
                if (stops_left > 0 or neighbour == dst):
                    heappush(heap, (total_price, stops_left - 1, neighbour))
        
        return -1