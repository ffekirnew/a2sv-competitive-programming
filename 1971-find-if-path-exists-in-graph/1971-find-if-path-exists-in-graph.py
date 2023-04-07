class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        # change the input into adjacency list
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        # define the dfs algorithm
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            
            for child in graph[node]:
                if child not in visited and dfs(child):
                    return True
        
        # return the solution
        visited = set()
        return dfs(source)
        