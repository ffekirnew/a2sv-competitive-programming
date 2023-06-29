from collections import defaultdict

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(set)
        
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        def dfs(node, probability, time):
            if node == target and time == t:
                return probability
            
            children = graph[node]
            if node == target and t > time and not children:
                return probability

            target_probability = 0
            for child in children:
                graph[child].remove(node)
                target_probability = max(dfs(child, probability / len(children), time + 1), target_probability)
            
            return target_probability
        
        return dfs(1, 1, 0)
        