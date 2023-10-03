from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        time_taken_from_k = [inf for _ in range(n)]
        time_taken_from_k[k - 1] = 0
        
        for from_, to_, weight in times:
            graph[from_][to_] = weight
        
        heap = [(0, k)] # (weight, node)[]
        visited = set([])
        
        while heap:
            weight, node = heappop(heap)
            visited.add(node)
            
            for child in graph[node].keys():
                if child not in visited and time_taken_from_k[child - 1] > weight + graph[node][child]:
                    time_taken_from_k[child - 1] = weight + graph[node][child]
                    
                    heappush(heap, (time_taken_from_k[child - 1], child))
        
        minimum_time = max(time_taken_from_k)
        return -1 if minimum_time == inf else minimum_time
                    
                    
                
        
        
        