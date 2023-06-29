from collections import defaultdict

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(set)
        
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        def dfs(node, probability, time, t):
            if node == target and time == t:
                return probability
            
            if node == target and t > time and len(graph[node]) == 0:
                return probability

            max_probability = 0
            for child in graph[node]:
                graph[child].remove(node)
                max_probability = max(dfs(child, probability / len(graph[node]), time + 1, t), max_probability)
            
            return max_probability
        
        return dfs(1, 1, 0, t)
        