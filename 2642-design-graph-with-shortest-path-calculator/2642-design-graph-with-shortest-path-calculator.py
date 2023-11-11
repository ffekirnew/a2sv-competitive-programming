from collections import defaultdict
from heapq import heappush, heappop


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(dict)
        for from_, to_, cost in edges:
            self.graph[from_][to_] = cost
        

    def addEdge(self, edge: List[int]) -> None:
        from_, to_, cost = edge
        self.graph[from_][to_] = cost
        

    def shortestPath(self, node1: int, node2: int) -> int:
        queue = [(0, node1)]
        visited = set()
        
        while queue:
            cost, node = heappop(queue)
            
            if node in visited:
                continue
            
            if node == node2:
                return cost
            
            visited.add(node)
            
            for neighbor, next_cost in self.graph[node].items():
                heappush(queue, (cost + next_cost, neighbor))
        
        return -1
            
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)