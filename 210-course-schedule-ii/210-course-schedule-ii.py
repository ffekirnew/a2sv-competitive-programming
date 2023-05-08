class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { i: [] for i in range(numCourses) }
        in_degree = { i: 0 for i in range(numCourses) }
        
        for course, pre_requisite in prerequisites:
            in_degree[course] += 1
            graph[pre_requisite].append(course)
            
        
        queue = deque([course for course in graph.keys() if in_degree[course] == 0])
        visited = set()
        path = []
        
        while queue:
            curr_course = queue.popleft()
            
            path.append(curr_course)
            visited.add(curr_course)
            
            for new_course in graph[curr_course]:
                if new_course in visited:
                    return []

                in_degree[new_course] -= 1
                
                if in_degree[new_course] == 0:
                    queue.append(new_course)

        if len(path) != numCourses:
            return []
        return path
            