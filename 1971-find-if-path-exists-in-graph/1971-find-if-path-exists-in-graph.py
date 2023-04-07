class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # change the input into adjacency list
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        # define the dfs algorithm
        def dfs(node, visited):
            if node == destination:
                return True
            
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    if dfs(child, visited):
                        return True
            
            return False
        
        # return the solution
        visited = set()
        return dfs(source, visited)
        