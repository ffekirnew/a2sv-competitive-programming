"""
Solution Steps:
1. Build the graph
2. Initialize all other nodes from the source with 0.0000 probability
3. Go from the source to the destination maximizing the probability (Dijkstra)

Complexity Analysis:
- Time: O(V + E) = 2 * 10 ** 4
- Space: O(v + E) = 2 * 10 ** 4
"""


from collections import defaultdict
from heapq import heappop, heappush


class PathWithMaximumProbability:
    def __init__(self, n: int, edges: List[List[int]], success_probabilities: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)
        for edge_index in range(len(edges)):
            node1, node2 = edges[edge_index]
            success_probability = success_probabilities[edge_index]
            
            self.graph[node1].append((node2, success_probability))
            self.graph[node2].append((node1, success_probability))
    
    def dijkstra(self, start_node: int, end_node: int) -> float:
        probabilities = [float(0) for _ in range(self.n)]
        probabilities[start_node] = float(1)

        queue = [(-1, start_node)]
        visited = set()
        while queue:
            probability, curr_node = heappop(queue)
            probability = -probability
            
            if curr_node == end_node:
                return probability
            
            if curr_node in visited:
                continue
            
            visited.add(curr_node)
            
            for next_node, next_probability in self.graph[curr_node]:
                new_probability = probability * next_probability
                if new_probability > probabilities[next_node]:
                    probabilities[next_node] = new_probability
                    heappush(queue, (-new_probability, next_node))
        
        return float(0)


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        solution = PathWithMaximumProbability(n, edges, succProb)
        return solution.dijkstra(start_node, end_node)