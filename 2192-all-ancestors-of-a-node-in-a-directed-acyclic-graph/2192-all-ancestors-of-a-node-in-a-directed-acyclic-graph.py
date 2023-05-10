class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i: set() for i in range(n)}
        in_coming = [0] * n
        
        for from_, to_ in edges:
            graph[from_].add(to_)
            in_coming[to_] += 1
        
        visited = set()
        ancestors = [ set() for i in range(n) ]
        
        queue = deque([ node for node in range(n) if in_coming[node] == 0 ])
        
        while queue:
            node = queue.popleft()

            visited.add(node)
            
            for child_node in graph[node]:
                if child_node in visited:
                    return []

                in_coming[child_node] -= 1
                for ancestor in ancestors[node]:
                    ancestors[child_node].add(ancestor)
                ancestors[child_node].add(node)
                
                if in_coming[child_node] == 0:
                    queue.append(child_node)
                    
        for i, ancestor in enumerate(ancestors):
            ancestors[i] = sorted(list(ancestor))

        return ancestors
        
            
        
        
        
            