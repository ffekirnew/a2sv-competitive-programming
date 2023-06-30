from collections import defaultdict

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(set)
        
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
            
        stack = [(1, 1, 0)]
        while stack:
            node, probability, time = stack.pop()

            if node == target and time == t:
                return probability
            
            children = graph[node]
            if node == target and t > time and not children:
                return probability

            for child in children:
                graph[child].remove(node)
                stack.append((child, probability / len(children), time + 1))
        
        return 0
        