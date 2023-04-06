class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        max_roads = 0
        graph = defaultdict(set)
        
        for road in roads:
            graph[road[0]].add(road[1])
            graph[road[1]].add(road[0])
        
        for i in range(n):
            for j in range(i + 1, n):
                max_roads = max( max_roads, len(graph[i]) + len(graph[j]) - (1 if i in graph[j] else 0) )
        
        return max_roads
        