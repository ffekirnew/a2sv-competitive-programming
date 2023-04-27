class Solution:
    @staticmethod
    def find_parents(graph):
        parents = {}

        visited = set([0])
        fringe = [0]

        while fringe:
            next_level = []

            for curr_node in fringe:
                for child in graph[curr_node][1]:
                    if child not in visited:
                        visited.add(child)
                        parents[child] = curr_node
                        next_level.append(child)

            fringe = next_level

        return parents
    
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = { i : [hasApple[i], []] for i in range(n)}
        
        for start, target in edges:
            graph[start][1].append(target)
            graph[target][1].append(start)

        parents = self.find_parents(graph)
        
        for i in range(n):
            if hasApple[i]:
                j = i
                while j in parents:
                    j = parents[j]
                    hasApple[j] = True
        
        # do the bfs
        fringe = []
        visited = set([0])
        
        if hasApple[0]:
            fringe = [0]
        
        time = 0
        while fringe:
            next_level = []
            
            for node in fringe:
                for child in graph[node][1]:
                    if child not in visited and hasApple[child]:
                        visited.add(child)
                        next_level.append(child)
                        time += 2
            
            fringe = next_level
        
        return time