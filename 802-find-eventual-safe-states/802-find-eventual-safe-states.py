import sys
sys.setrecursionlimit(1 << 30)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        new_graph = { i: [] for i in range(len(graph)) }
        in_degree = [0] * len(graph)
        
        for from_, edge in enumerate(graph):
            for to_ in edge:
                new_graph[to_].append(from_)
                in_degree[from_] += 1
        
        queue = deque([node for node in range(len(graph)) if not in_degree[node]])
        answer = []

        while queue:
            node = queue.popleft()
            answer.append(node)
            
            for child in new_graph[node]:
                in_degree[child] -= 1
                
                if not in_degree[child]:
                    queue.append(child)

        return sorted(answer)
        