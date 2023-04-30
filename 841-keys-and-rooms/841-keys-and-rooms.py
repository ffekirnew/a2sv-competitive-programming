class Solution:
    @staticmethod
    def buildGraph(edges):
        graph = defaultdict(list)
        
        for i, room in enumerate(edges):
            graph[i] = room.copy()
        
        return graph
    
    @staticmethod
    def bfs(graph, node):
        visited = set([node])
        fringe = [node]
        
        while fringe:
            next_level = []
            # do something
            
            for curr_node in fringe:
                for child in graph[curr_node]:
                    if child not in visited:
                        visited.add(child)
                        next_level.append(child)
            
            fringe = next_level
        
        return visited
        
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = self.buildGraph(rooms)
        visitable_rooms = self.bfs(graph, 0)
        
        return len(visitable_rooms) == len(rooms)
            
        