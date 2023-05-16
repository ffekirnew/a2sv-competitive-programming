class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph = {i: set() for i in range(n)}
        in_coming = [0] * n
        
        for from_, to_ in prerequisites:
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
                    
        answer = []
        for pre, course in queries:
            answer.append(pre in ancestors[course])
        
        return answer
            