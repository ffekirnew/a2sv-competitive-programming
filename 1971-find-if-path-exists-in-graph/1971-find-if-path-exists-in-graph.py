class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n <= 1:
            return True

        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        acquaintances = deque(graph[source])
        seen = set(acquaintances)
        
        while acquaintances:
            child = acquaintances.popleft()

            if child == destination:
                return True

            for acquaintance in graph[child]:
                if acquaintance not in seen:
                    acquaintances.append(acquaintance)
                    seen.add(acquaintance)
        
        return False
        