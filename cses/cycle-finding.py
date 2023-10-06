"""
Solution Steps:
1. Build the graph
2. Instantiate -inf costs to all nodes as distances and perform n - 1 relaxations (Bellman-Ford)
3. Check if there's a negative cycle using the nth relaxation
"""


from typing import List


class CycleFinding:
    def __init__(self, number_of_nodes: int, edges: List[int]):
        self.graph = [[] for _ in range(number_of_nodes + 1)]
        self.edges = edges

        for from_, to_, cost in edges:
            self.graph[from_].append((to_, cost))

    def solution(self):
        pass


if __name__ == '__main__':
    number_of_nodes, number_of_edges = list(map(int, input().split()))
    edges = []
    for _ in range(number_of_edges):
        edges.append(list(map(int, input().split())))

    solution = CycleFinding(number_of_nodes, edges)
    solution.solution()