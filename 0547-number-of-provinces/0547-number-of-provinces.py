class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    graph[i + 1].add(j + 1)
        
        nodes = set(graph.keys())
        visited = set()
        def dfs(node):
            visited.add(node)
            
            for child in graph[node]:
                if child not in visited:
                    dfs(child)
        
        answer = 0
        for node in nodes:
            if node not in visited:
                dfs(node)
                answer += 1
        
        return answer
        
        
                
            
        