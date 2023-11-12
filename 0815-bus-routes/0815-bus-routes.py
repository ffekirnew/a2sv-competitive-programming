class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(set)
        source_busses = set()
        target_busses = set()
        
        for i in range(len(routes)):
            routes[i] = set(routes[i])
            
            if source in routes[i]:
                source_busses.add(i)

            if target in routes[i]:
                target_busses.add(i)
        
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if routes[i].intersection(routes[j]):
                    graph[i].add(j)
                    graph[j].add(i)
        
        min_length = inf
        queue = deque([[bus, 1] for bus in source_busses])
        visited = set([bus for bus in source_busses])
        
        while queue:
            bus, busses_used = queue.popleft()
            
            if bus in target_busses:
                min_length = min( min_length, busses_used )
                continue
            
            for new_bus in graph[bus]:
                if new_bus not in visited:
                    visited.add(new_bus)
                    queue.append([new_bus, busses_used + 1])
                    
        
        if min_length == inf:
            return -1
        
        return min_length
            
            
        