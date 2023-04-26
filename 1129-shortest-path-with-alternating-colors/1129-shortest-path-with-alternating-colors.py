class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = { node: [] for node in range(n) }
        
        for start, dest in redEdges:
            graph[start].append((dest, 0))
        
        for start, dest in  blueEdges:
            graph[start].append((dest, 1))
        
        def bfs(target):
            visited = set([0, None])
            fringe = [(0, None, [])]
            
            while fringe:
                next_level = []
                
                for curr_node, curr_color, curr_path in fringe:
                    if curr_node == target:
                        return len(curr_path)

                    for child, color in graph[curr_node]:
                        if (curr_color == None or color != curr_color) and (child, color) not in visited:
                            visited.add((child, color))
                            next_level.append((child, color, curr_path + [child]))
                    
                fringe = next_level
            return -1
        
        answer = []
        for i in range(n):
            answer.append(bfs(i))
        
        return answer
            
                    
            
            
            
            
            